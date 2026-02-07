from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
import numpy as np
import cv2 as cv
from PIL import Image
import io
import base64
import os

from backend.recognize_service import detect_faces, predict_faces_and_annotate
from backend.model_service import model_service

app = FastAPI(title="Autism Screening API")

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Data Models ---

class QuestionnaireInput(BaseModel):
    answers: List[int] # Expects 10 binary answers (0 or 1)
    age_months: int
    sex: int # 1 for Male, 0 for Female
    jaundice: int # 1 for Yes, 0 for No
    family_asd: int # 1 for Yes, 0 for No

class Center(BaseModel):
    name: str
    link: str

# --- Routes ---

@app.get("/api/health")
def health_check():
    return {"status": "ok"}

@app.post("/api/predict/image")
async def predict_image(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        img = cv.imdecode(nparr, cv.IMREAD_COLOR)
        
        if img is None:
             raise HTTPException(status_code=400, detail="Invalid image file")

        # Detect faces
        faces, gray = detect_faces(img)
        
        if len(faces) == 0:
            return {
                "success": False,
                "message": "No face detected. Please upload a clear image."
            }
        
        # Predict and annotate
        result_img, predictions = predict_faces_and_annotate(img, faces, gray)
        
        # specific logic for result
        # The existing logic just printed label/confidence on image.
        # We can also infer a general "Screening Result" if needed, 
        # but for now we follow the visual output style.
        
        # Convert result image to base64 to display on frontend
        _, buffer = cv.imencode('.jpg', result_img)
        img_base64 = base64.b64encode(buffer).decode('utf-8')
        
        return {
            "success": True,
            "predictions": predictions,
            "annotated_image": f"data:image/jpeg;base64,{img_base64}"
        }

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/predict/questionnaire")
def predict_questionnaire(data: QuestionnaireInput):
    try:
        # Construct the 14-element list
        # ['A1'...'A10', 'Age','Sex','Jaundice','Family_ASD']
        input_features = data.answers + [data.age_months, data.sex, data.jaundice, data.family_asd]
        
        result = model_service.predict(input_features)
        
        # result is now a dict: {"prediction": int, "impressions": list}
        prediction = result["prediction"]
        impressions = result["impressions"]
        
        # prediction 1 = ASD Traits Detected, 0 = No
        return {
            "asd_traits_detected": bool(prediction == 1),
            "message": "ASD Traits Detected" if prediction == 1 else "No ASD Traits Detected",
            "impressions": impressions
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/centers/{city}")
def get_centers(city: str):
    # Sample data ported from web1.py
    autism_centers = {
        "Mumbai": [
            {"name": "Ummeed Child Development Center", "link": "https://ummeed.org"},
            {"name": "Sethu Center", "link": "https://sethu.in"}
        ],
        "Delhi": [
            {"name": "Action for Autism", "link": "https://actionforautism.org"},
            {"name": "VIMHANS", "link": "https://vimhans.com"}
        ],
        "Pune": [
            {"name": "Sparsh Autism Center", "link": "https://sparshpune.org"}
        ]
    }
    
    # Simple normalization
    city_key = city.capitalize()
    if city_key in autism_centers:
        return autism_centers[city_key]
    else:
        return [] # Or raise 404

# Serve frontend static files
# We assume 'frontend' folder is at the same level as 'backend'
# Path: e:\Degree_txt_books\SEM-6\project\frontend
frontend_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "frontend")
if os.path.exists(frontend_path):
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

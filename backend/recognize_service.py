import cv2 as cv
import numpy as np
import os

# Helper to load resources safely
def get_resource_path(filename):
    # Assuming resources are in the parent directory or same dir for now, 
    # but based on existing project structure, they are in the root 'project' folder.
    # Since this file is in 'backend/', we need to go up one level.
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, filename)

# Load resources once (global scope for simplicity in this script, 
# in a larger app we might wrap in a class or startup event)
try:
    # Use cv2's built-in haar cascade if specific file not found, or try the local one
    cascade_path = cv.data.haarcascades + 'haarcascade_frontalface_default.xml'
    # Or fallback to previous hardcoded one if user really wants it, but `cv.data` is safer.
    
    haar = cv.CascadeClassifier(cascade_path)
    
    # Load recognizer
    recognizer_path = get_resource_path("autism_recognizer.yml")
    faces_recog = cv.face.LBPHFaceRecognizer_create(radius=1, neighbors=8, grid_x=8, grid_y=8)
    
    if os.path.exists(recognizer_path):
        faces_recog.read(recognizer_path)
    else:
        print(f"Warning: autism_recognizer.yml not found at {recognizer_path}")

except Exception as e:
    print(f"Error loading models: {e}")

child = ["Autistic", "Non Autistic"]

def detect_faces(image_np):
    gray = cv.cvtColor(image_np, cv.COLOR_BGR2GRAY)    
    detected_faces = haar.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=7,
        minSize=(80, 80)
    )
    return detected_faces, gray

def predict_faces_and_annotate(image_np, detected_faces, gray):
    # Work on a copy to avoid modifying original array in place if needed elsewhere
    result_image = image_np.copy()
    
    predictions = []
    
    for (x, y, w, h) in detected_faces:
        face_roi = gray[y:y+h, x:x+w]
        face_resized = cv.resize(face_roi, (150, 150))
        # Ensure correct type
        face_resized = np.array(face_resized, dtype=np.uint8)
        
        label, confidence = faces_recog.predict(face_resized)
        
        # Safe access to child list
        pred_label = child[label] if label < len(child) else "Unknown"
        text = f"{pred_label} ({confidence:.2f})"
        
        color = (0, 255, 0) # Green
        cv.rectangle(result_image, (x, y), (x+w, y+h), color, 2)
        cv.putText(result_image, text, (x, y-6), cv.FONT_HERSHEY_COMPLEX, 0.5, color, 2)
        
        predictions.append({
            "box": [int(x), int(y), int(w), int(h)],
            "label": pred_label,
            "confidence": float(confidence)
        })
        
    return result_image, predictions

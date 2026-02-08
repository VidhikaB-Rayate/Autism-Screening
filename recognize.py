import cv2 as cv
import numpy as np  

import os

def get_path(filename):
    # Get the directory where recognize.py is located
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, filename)

child = ["Autistic", "Non Autistic"]

# Load Haar Cascade
cascade_path = get_path("haar_cascade.xml")
if os.path.exists(cascade_path):
    haar = cv.CascadeClassifier(cascade_path)
    print(f"Haar cascade loaded from: {cascade_path}")
else:
    print(f"ERROR: haar_cascade.xml not found at {cascade_path}")
    haar = None

# Load LBPH Face Recognizer
faces_recog = cv.face.LBPHFaceRecognizer_create(radius=1, neighbors=8, grid_x=8, grid_y=8)
recognizer_path = get_path("autism_Recognizer.yml")

if os.path.exists(recognizer_path):
    try:
        faces_recog.read(recognizer_path)
        print(f"LBPH Recognizer loaded from: {recognizer_path}")
    except Exception as e:
        print(f"ERROR reading LBPH model: {e}")
        faces_recog = None
else:
    print(f"ERROR: autism_Recognizer.yml not found at {recognizer_path}")
    faces_recog = None

def detect_faces(image):
    if haar is None:
        print("detect_faces: haar cascade is not loaded")
        return [], None
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)    
    detected_faces = haar.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=7,
        minSize=(80, 80)
    )
    return detected_faces, gray


def predict_faces(image, detected_faces, gray):
    for (x, y, w, h) in detected_faces:
        face_roi = gray[y:y+h, x:x+w]
        face_resized = cv.resize(face_roi, (150, 150))
        face_resized = np.array(face_resized, dtype=np.uint8)
        
        if faces_recog is not None:
            label, confidence = faces_recog.predict(face_resized)
            text = f"{child[label]} ({confidence:.2f})"
        else:
            text = "Model Missing"
            confidence = 0
            
        color = (0, 255, 0)
        cv.rectangle(image, (x, y), (x+w, y+h), color, 2)
        cv.putText( image, text, (x, y-6), cv.FONT_HERSHEY_COMPLEX, 0.5, color, 2)
    return image

# img = cv.imread(r"E:\Degree_txt_books\SEM-6\Report\gauri.jpeg")

# detected_faces, gray = detect_faces(img)
# result = predict_faces(img, detected_faces, gray)

# cv.imshow("Detected Face", result)
# cv.waitKey(0)
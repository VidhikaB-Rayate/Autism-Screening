import cv2 as cv
import numpy as np  

child = ["Autistic", "Non Autistic"]

haar = cv.CascadeClassifier(r"E:\Explore\OpenCV\haar_cascade.xml")
faces_recog = cv.face.LBPHFaceRecognizer_create(radius=1, neighbors=8, grid_x=8, grid_y=8)
faces_recog.read(r"autism_recognizer.yml")

def detect_faces(image):
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
        label, confidence = faces_recog.predict(face_resized)
        text = f"{child[label]} ({confidence:.2f})"
        color = (0, 255, 0)
        cv.rectangle(image, (x, y), (x+w, y+h), color, 2)
        cv.putText( image, text, (x, y-6), cv.FONT_HERSHEY_COMPLEX, 0.5, color, 2)
    return image

# img = cv.imread(r"E:\Degree_txt_books\SEM-6\Report\gauri.jpeg")

# detected_faces, gray = detect_faces(img)
# result = predict_faces(img, detected_faces, gray)

# cv.imshow("Detected Face", result)
# cv.waitKey(0)
import os
import cv2 as cv
import numpy as np

dir = r"E:\Degree_txt_books\SEM-6\project\train"
haar_dir = r"E:\Explore\OpenCV\haar_cascade.xml"
haar = cv.CascadeClassifier(haar_dir)
classes = sorted(os.listdir(dir))

features = []
labels = []

def create_training_data():
    for label, class_name in enumerate(classes):
        class_path = os.path.join(dir, class_name)

        for img_name in os.listdir(class_path):
            img_path = os.path.join(class_path, img_name)
            image = cv.imread(img_path)
            gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            faces = haar.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=7, minSize=(80, 80))
            
            for (x, y, w, h) in faces:
                face_roi = gray[y:y+h, x:x+w]
                resized = cv.resize(face_roi, (150, 150))
                normalized = resized / 255.0  
                features.append(normalized)
                labels.append(label)

create_training_data()

print("Training data created successfully.")
print("Total samples:", len(features))

features = np.array(features, dtype="float32")
labels = np.array(labels)

recog = cv.face.LBPHFaceRecognizer_create()
recog.train(features, labels) 
recog.save(r"autism_Recognizer.yml")
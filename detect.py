import cv2
import numpy as np
import pickle
import os
from datetime import datetime



os.system("test.py")
face_classifier = cv2.CascadeClassifier('C:/Users/Suparshaw Singh/AppData/Local/Programs/Python/Python39/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
recognizer= cv2.face.LBPHFaceRecognizer_create()
recognizer.read("test.yml")
eye_classifier=cv2.CascadeClassifier('C:/Users/Suparshaw Singh/AppData/Local/Programs/Python/Python39/Lib/site-packages/cv2/data/haarcascade_eye.xml')

label={}
with open("label.pickle",'rb') as f:
    og_label =pickle.load(f)
    label={v:k for k,v in og_label.items()}




def markattendance(name):
    with open("attendance.csv",'r+') as f:
        mydata=f.readlines()
        namelist=[]
        for line in mydata:
            entry = line.split(",")
            namelist.append(entry[0])
        if name not in namelist:
            today= datetime.today()
            tdstring= today.strftime("%d/%b/%y")
            now=datetime.now()
            tymstring= now.strftime("%H:%M:%S")
            f.writelines(f'\n {name},{tdstring},{tymstring},{"P"}')


def face_detector(img, size = 0.5):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)

    if faces is():
        return img,[]

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)
        roi_color = img[y:y+h, x:x+w]
        roi = cv2.resize(roi_color, (200,200))
        eyes = eye_classifier.detectMultiScale(roi_color)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    return img,roi

def detect():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()

        image, face = face_detector(frame)



        try:
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            id_,confidence=recognizer.predict(face)
            name=label[id_]




            if confidence > 80:
                cv2.putText(image, name, (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)
                cv2.imshow('Face Cropper', image)
                markattendance(name)


            else:
                cv2.putText(image, "Unknown", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                cv2.imshow('Face Cropper', image)


        except:
            cv2.putText(image, "Face Not Found", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
            cv2.imshow('Face Cropper', image)
            pass

        if cv2.waitKey(1)==13:
            break


    cap.release()
    cv2.destroyAllWindows()

detect()

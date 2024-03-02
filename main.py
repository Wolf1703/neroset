import time

import cv2

vid = cv2.VideoCapture(0)
while True:
    success, img6 = vid.read()
    smile = cv2.CascadeClassifier('smile.xml')
    result3 = smile.detectMultiScale(img6, scaleFactor=1.1, minNeighbors=50)
    for (x, y, w, h) in result3:
        rec = cv2.rectangle(img6, (x, y), (x + w, y + h), (255, 0, 0), thickness=3)
        cv2.imshow('g', img6)
    eyes = cv2.CascadeClassifier('eye.xml')
    result2 = eyes.detectMultiScale(img6, scaleFactor=1.1, minNeighbors=8)
    for (x, y, w, h) in result2:
        rec = cv2.rectangle(img6, (x, y), (x + w, y + h), (0, 255, 0), thickness=3)
        cv2.imshow('g', img6)
    faces = cv2.CascadeClassifier('face.xml')
    result = faces.detectMultiScale(img6, scaleFactor=1.1, minNeighbors=3)
    print(result)
    for (x, y, w, h) in result:
        rec = cv2.rectangle(img6, (x, y), (x + w, y + h), (0, 0, 255), thickness=3)
        cv2.imshow('g', img6)
    if cv2.waitKey(100) and 0xFF == ord("q"):
        break


cv2.waitKey(0)


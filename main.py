import time
import pygame
import cv2

vid = cv2.VideoCapture(0)
num = 0
while True:
    success, img6 = vid.read()
    smile = cv2.CascadeClassifier('smile.xml')
    result3 = smile.detectMultiScale(img6, scaleFactor=2, minNeighbors=35)
    cv2.imshow('g', img6)
    for (x, y, w, h) in result3:
        rec = cv2.rectangle(img6, (x, y), (x + w, y + h), (255, 0, 0), thickness=3)
        cv2.imshow('g', img6)
        num += 1
        print(num)
        if num > 12:
            quit()
        else:
            break
    if cv2.waitKey(100) and 0xFF == ord("q"):
        break

cv2.waitKey(0)

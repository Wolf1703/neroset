import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:

    success, img = cap.read()
    a = img
    b = a
    c = b
    a = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    cv2.imshow('green', a)

    b = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # kernel = np.ones((15, 15), np.uint8)
    # img = cv2.dilate(img, kernel, iterations=1)
    # img = cv2.erode(img, kernel, iterations=1)
    cv2.imshow('HELL', b)

    # img = cv2.calibrateCamera(1)
    c = cv2.cvtColor(img, cv2.COLOR_BGR2LUV)
    cv2.imshow("luv", c)

    img = cv2.Canny(img, 100, 100)
    cv2.imshow("black", img)
    if cv2.waitKey(100) and 0xFF == ord("q"):
        break
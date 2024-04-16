import cv2
import time
import os
wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

folderPath = "FingerImages"
myList = os.listdir(folderPath)
print(myList)
while True:
    success, img = cap.read()
    cv2.imshow("Image", img)
    cv2.waitKey(1)
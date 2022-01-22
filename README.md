# Comp-vision
Computer-vision project
import cvzone
from cvzone.HandTrackingModule import HandDetector
import numpy
import cv2
cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,780)
detector=HandDetector(detectionCon=0.8,maxHands=2)
color = (0, 255, 0)
x = 100
y = 200
w = 300
h = 400
while True:

    success,img=cap.read()
    cv2.rectangle(img,(x,y),(w,h),color,cv2.FILLED)
    Hands,img= detector.findHands(img)
    if Hands:
        Hands1=Hands[0]
        lmlist=Hands1['lmList']
        cursor=lmlist[8]
        lenght,info,img=detector.findDistance(lmlist[8],lmlist[12],img)
        if x<cursor[0]<w and y<cursor[1]<h and lenght<30:
                color = (0, 255, 255)
                x=cursor[0]/2
                y=cursor[1]/2
                w=x+200
                h=y+200


    cv2.imshow("image",img)
    cv2.waitKey(1)

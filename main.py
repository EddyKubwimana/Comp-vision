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
w = 150
h = 250
while True:

    success,img=cap.read()

    Hands,img= detector.findHands(img)
    class mytryiangle():
        def __init__(self,x,y,w,h):
            self.x=x
            self.y=y
            self.w=w
            self.h=h

    if Hands:
        Hands1=Hands[0]
        lmlist=Hands1['lmList']
        cursor=lmlist[8]
        lenght,info,img=detector.findDistance(lmlist[8],lmlist[12],img)
        if x-w//2 <cursor[0]< x+w//2 and y-h//2 <cursor[1]<y+h//2 and lenght<=30:
                color = (0, 255, 255)
                x,y=cursor
        else:
            color=(0, 255, 0)
    cv2.rectangle(img, (x-w//2, y-h//2), (x+w//2, y+h//2), color, cv2.FILLED)

    cv2.imshow("image",img)
    cv2.waitKey(1)
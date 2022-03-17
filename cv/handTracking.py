import cv2
import mediapipe as mp
import numpy as np
import time

cap = cv2.VideoCapture(0)
myHands = mp.solutions.hands
hands = myHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime=0
cTime=0
fps=1
while True:
    success,img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            for id, lm in enumerate(handlms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)
                # if id == 4:
                cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(img,handlms,myHands.HAND_CONNECTIONS)

    cTime = time.time()
    try:
        fps = 1 / (cTime - pTime)
        pTime = cTime
    except:
        pass

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,(255, 0, 255), 3)
    cv2.imshow('Frame',img)
    cv2.waitKey(1)
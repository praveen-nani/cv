import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract"
img = cv2.imread('1.jpeg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
imgr=img[750:1100,:]
imgr=cv2.imread('3.jpg')
imgr = cv2.cvtColor(imgr,cv2.COLOR_BGR2RGB)
imgr=cv2.resize(imgr,(500,400))
hImg,wImg,_ =imgr.shape
boxes = pytesseract.image_to_boxes(imgr)
for b in boxes.splitlines():
    print(b)
    b=b.split(' ')
    print(b)
    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(imgr,(x,hImg-y),(w,hImg-h),(250,50,55),2)
    cv2.putText(imgr,b[0],(x,hImg-y+25),cv2.FONT_ITALIC,1,(250,0,250),1)
cv2.imshow("word",imgr)
cv2.waitKey(0)
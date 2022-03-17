import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract"
#img = cv2.imread('1.jpeg')
#imgr=img[750:1100,:]
imgr=cv2.imread('3.jpg')
imgr = cv2.cvtColor(imgr,cv2.COLOR_BGR2RGB)
imgr=cv2.resize(imgr,(500,400))

boxes = pytesseract.image_to_data(imgr)
for a,b in enumerate(boxes.splitlines()):
    print(a,b)
    if a!=0:
        b=b.split()
        if len(b)==12:
            x,y,w,h =int(b[6]),int(b[7]),int(b[8]),int(b[9])
            cv2.putText(imgr,b[11],(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,0),1)
            cv2.rectangle(imgr,(x,y),(x+w,y+h),(255,255,0),2)

cv2.imshow('img',imgr)
cv2.waitKey(0)
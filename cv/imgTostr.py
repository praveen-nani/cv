import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract"
img = cv2.imread('1.jpeg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
imgr=img[750:1100,:]
print(pytesseract.image_to_string(imgr))
cv2.imshow('img',imgr)
cv2.waitKey(0)
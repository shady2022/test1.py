from typing import Text
import cv2
import pytesseract
import numpy as np 
from PIL import Image


video_cap = cv2.VideoCapture(1)

while True:
    ret, image = video_cap.read()
    cv2.imshow("text detection", image)
    if cv2.waitKey(1)& 0xFF== ord("s"):
        cv2.imwrite("test1.jpg", image)
        break
    
video_cap.release()
cv2.destroyAllWindows()

def tesseract():
    pytesseract.pytesseract.tesseract_cmd = "D:\\Python Project\\kar\\Tesseract-OCR\\tesseract.exe" 
    image_path = cv2.imread("test1.jpg")
    gray = cv2.cvtColor(image_path, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)[1]
    h, w = gray.shape
    
    gray = cv2.rotate(gray, cv2.ROTATE_90_COUNTERCLOCKWISE)
    config = '--psm 6 -c tessedit_char_whitelist="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "'
    text = pytesseract.image_to_string(gray, config=config)
    print(text.replace('\n', '').replace('\f', ''))

tesseract()

def save():
    pytesseract.pytesseract.tesseract_cmd = "D:\\Python Project\\kar\\Tesseract-OCR\\tesseract.exe" 
    image_path = cv2.imread("test1.jpg")
    change = cv2.resize(image_path, None, fx=0.5, fy=0.5)
    gray = cv2.cvtColor(change, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)[1]
    h, w = gray.shape
    
    gray = cv2.rotate(gray, cv2.ROTATE_90_COUNTERCLOCKWISE)
   
    text = pytesseract.image_to_string(gray)
    
    out = open("codes.csv", "w", newline="")
    out.write(text)
    out.close()
    exit()
    
save()


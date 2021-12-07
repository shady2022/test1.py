from typing import Text
import cv2
import pytesseract
import numpy as np 
import csv
from PIL import Image
#from PySide6.QtWidgets import *
#from PySide6.QtUiTools import *
#from PySide6.QtCore import *

#class MAIN(QMainWindow):
    #def __init__(self):
        #super().__init__()
        #loader = QUiLoader()
        #self.ui = loader.load('new.ui',None)
        #self.ui.show()
        #self.ui.btn1.clicked.connect(self.start)

f = open("codes.csv", "r")
header = ("code")
data = f.read()
data = data.split('\n')
print(data," ******")

video_cap = cv2.VideoCapture(1)

while True:
    ret, image = video_cap.read()
    camera = image[150:300,250:400]
    cv2.imshow("text detection", camera)
    if cv2.waitKey(1)& 0xFF== ord("s"):
        cv2.imwrite("test1.jpg", camera)
        break
  
video_cap.release()
cv2.destroyAllWindows()

def main():
    img = cv2.imread("test1.jpg")

    pytesseract.pytesseract.tesseract_cmd = "D:\\Python Project\\kar\\Tesseract-OCR\\tesseract.exe"

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)[1]
    h, w = gray.shape

    gray = cv2.rotate(gray, cv2.ROTATE_90_COUNTERCLOCKWISE)
    gray = cv2.warpPolar(gray, (-1, -1), (h // 2, h // 2), h // 2,
                        cv2.INTER_CUBIC + cv2.WARP_POLAR_LINEAR)

    gray = cv2.rotate(gray, cv2.ROTATE_90_COUNTERCLOCKWISE)

    config = '--psm 6 -c tessedit_char_whitelist="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "'

    text = pytesseract.image_to_string(gray, config=config)
    print(text)
    data.append(text)
    
    out = open('codes.csv', 'w')
    for d in data:
        out.write(d)
        if d != data[-1]:
            out.write('\n')
    out.close()
    
main()
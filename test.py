import cv2
import pytesseract

# Read image
img = cv2.imread('NEW.jpg')

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Desktop\\image processing python\\Tesseract-OCR\\tesseract.exe'


# Convert to grayscale, and binarize, especially for removing JPG artifacts
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)[1]
h, w = gray.shape

# If specifically needed, also remove text in the original image
# Contour index 0 = inner edge of inner circle (to keep inner circle itself)
#img[:, l:l+h] = cv2.drawContours(img[:, l:l+h], cnts, 0, (255, 255, 255), cv2.FILLED)

# Rotate image before remapping to polar coordinate space to maintain
# circular text en bloc after remapping
gray = cv2.rotate(gray, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Actual remapping to polar coordinate space
gray = cv2.warpPolar(gray, (-1, -1), (h // 2, h // 2), h // 2,
                     cv2.INTER_CUBIC + cv2.WARP_POLAR_LINEAR)

# Rotate result for OCR
gray = cv2.rotate(gray, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Actual OCR, limiting to capital letters only
config = '--psm 6 -c tessedit_char_whitelist="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "'

text = pytesseract.image_to_string(gray, config=config)
print(text.replace('\n', '').replace('\f', ''))


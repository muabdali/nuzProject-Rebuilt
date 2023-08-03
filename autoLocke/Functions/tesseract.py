import pytesseract
import cv2
import numpy as np

# Python file dedicated to enhancing, reading, and returning given images.

class imgProcess():
    def __init__(self):
        return
    def imageEnhance(self, imagePath):
        img = cv2.imread(imagePath)
        hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower_white = np.array([0, 0, 200], dtype=np.uint8)
        upper_white = np.array([255, 25, 255], dtype=np.uint8)
        white_mask = cv2.inRange(hsv_image, lower_white, upper_white)
        result = cv2.bitwise_and(img, img, mask=~white_mask)
        print(pytesseract.image_to_string(result))

ia = imgProcess()
ia.imageEnhance(imagePath='autoLocke/Files/Images/ocrTests/Route1FireRed.png')

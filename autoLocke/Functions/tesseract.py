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
        finalImage = cv2.bitwise_and(img, img, mask=~white_mask)
        result = pytesseract.image_to_string(image=finalImage)
        return result

"""
ia = imgProcess()
ia.imageEnhance(imagePath='autoLocke/Files/Images/ocrTests/Route1FireRed.png')


imageEnhance contains one input variable, which is imagePath.
The imagePath variable should be the path to the image that needs to be processed and extracted.

the enhance process is simple, all it does is remove the white background and possibly the gray dropshadow.
This seems to be enough for fire red routes. 


"""
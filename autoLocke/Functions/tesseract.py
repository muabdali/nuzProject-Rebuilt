import pytesseract
import cv2

# Python file dedicated to enhancing, reading, and returning given images.

class imgProcess():
    def __init__(self):
        return
    def imageEnhance(self, imagePath):
        img = cv2.imread(imagePath)
        img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
        print(pytesseract.image_to_string(img))

ia = imgProcess()
ia.imageEnhance(imagePath='autoLocke/Files/Images/ocrTests/PalletTown.png')

import numpy as np
import cv2

#create image
def createImg(height, width):
    return np.zeros((height, width, 3), np.uint8)

#display image
def dispImg(img):
    cv2.imshow('Image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
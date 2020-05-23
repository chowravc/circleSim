import cv2
import numpy as np
import render as r

def intRound(image):
    out = np.ones(image.shape, np.uint8)
    for i in range(len(image)):
        for j in range(len(image[0])):
            for k in range(len(image[0][0])):
                if image[i][j][k] == np.Inf:
                    out[i][j][k] = 255
                else:
                    out[i][j][k] = int(image[i][j][k])
    return out
                
def normalize(image, depth, rounded=True):
    norm = (depth*(image - image.mean())/(image.std())) + 128
    if rounded:
        return intRound(norm)
    else:
        return norm

def addNoise(image, depth, intensity):    
    norm = normalize(image, depth, False)
    noisy = intRound(norm + (24*intensity/255) * norm.std() * np.random.random(norm.shape))
    return noisy
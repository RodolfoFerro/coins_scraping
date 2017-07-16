# =========================================================
# Harvard University
# Authors: 
#     Rodolfo Ferro Pérez (ferro@cimat.mx)
#     Carlos Outeiral Rubiera (couteiral@gmail.com)
#     Daniel Haas (dih16@hampshire.edu)
#
# Basic image utilities library for imgs pre-processing.
# =========================================================


# =========================================================
# Importing our libs:
# =========================================================
import cv2
import numpy as np
import random
from itertools import chain

# =========================================================
# Defining or funtions:
# =========================================================

# =========================================================
# MAIN
# =========================================================

if __name__ == '__main__':
def scaleImg(img):
    return cv2.resize(img, (128, 128), interpolation = cv2.INTER_AREA)

def rotateImage(img):
    angle = random.gauss(180, 90)
    rotMatrix = cv2.getRotationMatrix2D((64, 64), angle, 1)
    return cv2.warpAffine(img, rotMatrix, (128, 128))

def addNoise(img):
    nAffectedPixels = int(random.gauss(1600, 500))
    pixelsLocation = np.random.randint(0, 128, [nAffectedPixels, 2])
    rgb = np.random.randint(0, 255, [nAffectedPixels, 3])
    for k, loc in enumerate(pixelsLocation):
        img[loc.item(0)][loc.item(1)] = rgb.item(k)
    return img

def removeBlackBorder(img):
    for i in range(128):
        whiteStarts = 0
        whiteEnds = 0
        for j in range(128):
            whiteStarts +=1
            if all(i >= 4 for i in img[j][i]):
                whiteEnds = whiteStarts
                break
        for j in range(whiteStarts, 128):
            if all(i <= 4 for i in img[j][i]):
                whiteEnds -= 1
                break
            whiteEnds += 1
        blackInterval = chain(range(0, whiteStarts), range(whiteEnds, 128))
        for j in blackInterval:
            img[j][i] = [255, 255, 255]
    return img

def blurImage(img, n):
    kernel = np.ones((n, n), np.float32)/n**2
    dist = cv2.filter2D(img, -1, kernel)
    return dist

def edgeGradient(img, sigma=0.33):
	med = np.median(img)
	low, upp  = int(max(0, (1.0-sigma)*med)), int(min(255, (1.0+sigma)*med))
	edg  = cv2.Canny(img, low, upp)
	return edg

def adjustGamma(image, gamma=1.0):
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
	return cv2.LUT(image, table)


# =========================================================
# MAIN
# =========================================================

if __name__ == '__main__':
    print("Here!")
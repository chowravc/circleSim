import cv2
import random
import numpy as np
import datetime
import os

import circle as c
import perlinNoise as pN
import render as r

def generateImages(height, width, minCircles, maxCircles, minRadius, maxRadius, numImages):

	root = os.getcwd()
	os.mkdir(root + "/output/")

	circleSets = []

	startTime = datetime.datetime.now()
	islandLocations = []
	imgs = []

	for i in range(numImages):

		img = r.createImg(height, width)

		circles = []
		array = np.zeros((height, width))

		tempCircles = random.randint(minCircles, maxCircles)

		for j in range(tempCircles):

			circles.append(c.nonIntersectingCircle(circles, height, width, minRadius, maxRadius))

			img = circles[-1].draw(img)

			array = circles[-1].pixelLocation(array)

		islandLocations.append(array)
		islandLocation = islandLocations[-1]

		cv2.imwrite(root + '/output/img_' + repr(i+1) + '.jpg', img)
		np.savetxt(root + '/output/img_' + repr(i+1) + '.txt', islandLocation)

	#Printing how long the circles took to create
	endTime = datetime.datetime.now()
	print("Time taken for " + repr(numImages) + " images: " +  repr(endTime - startTime))
	print("Time per image: " + repr((endTime - startTime)/numImages))
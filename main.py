import cv2
import random
import numpy as np
import datetime
import os

import circle as c
import render as r
import smartNoise.noiseExtractor as nE
import artifacts.addArtifacts as aA

def generateImages(height, width, minCircles, maxCircles, minRadius, maxRadius, numImages, ext):

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

		cv2.imwrite(root + '/output/img_' + repr(i+1) + '.' + ext, img)
		np.savetxt(root + '/output/img_' + repr(i+1) + '.txt', islandLocation)

	#Printing how long the circles took to create
	endTime = datetime.datetime.now()
	print("Time taken for " + repr(numImages) + " images: " +  repr(endTime - startTime))
	print("Time per image: " + repr((endTime - startTime)/numImages))

def extractSmartNoise(crop, cropManual, cropX, cropY):

	home = os.getcwd()

	noiseSamplePath = "/smartNoise/noiseSamples/"

	nE.noiseExtractor(home, noiseSamplePath, crop, cropManual, cropX, cropY)

def enchanceImages(runName, imgMean, imgStd, gaussian, doSmartNoise, smartNoise, numCircles, addGrid, gridRange, stds):

	print("Enhancing Simulation Images")

	# Home directory of sett2.
	home = os.getcwd()

	# Path to addArtifacts.py
	path = home + "/artifacts/"

	# Path to smart noise image files.
	smartNoisePath = "smartNoise/noiseSamples/noiseFiles"

	# Calling function addArtifacts.
	aA.addArtifacts(home, runName, imgMean, imgStd, gaussian, doSmartNoise, smartNoisePath, smartNoise, numCircles, addGrid, gridRange, stds)

if __name__ == "__main__":

	#generateImages(572, 572, 20, 40, 20, 40, 1, "tif")

	crop = True # Uses preprogrammed crop limits.
	cropManual = False # Crop Manuall (False recommended).
	cropX = [200,600] # Sets the x crop limits if cropManual is no.
	cropY = [200,600] # Sets the y crop limits if cropManual is no.
	#extractSmartNoise(crop, cropManual, cropX, cropY)

	imgMeanMin = 0.3
	imgMeanMax = 0.7
	imgMean = [imgMeanMin, imgMeanMax]

	imgStdMin = 1
	imgStdMax = 24
	imgStd = [imgStdMin, imgStdMax]

	gaussianMin = 0 # in units of sigma
	gaussianMax = 1.5
	gaussian = [gaussianMin, gaussianMax]

	doSmartNoise = True # yes if you wish to add smart noise extracted from real images
	smartNoiseMin = 0.3
	smartNoiseMax = 2.5
	smartNoise = [smartNoiseMin, smartNoiseMax]

	numCircles = 0 # overlays circles of random brightness on images. 0 to not add in circles

	addGrid = True # splits images into four random quadrants, which each have their brightness randomly changed

	gridRange = 0.5 # range over which a quadrant can be brightened or dimmed

	stds = 6 # Dynamic range of standardised image

	runName = "/output/"

	enchanceImages(runName, imgMean, imgStd, gaussian, doSmartNoise, smartNoise, numCircles, addGrid, gridRange, stds)
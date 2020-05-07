import cv2
import os.path
import numpy as np
import datetime

import circle as c
import render as r

#Number of images to create
numImages = 1000

#height of image
height = 480

#width of image
width = 704

#Number of circles per image
numberOfCircles = 20

#Minimum radius and Maximum radius of circles
minRadius = 20
maxRadius = 30

dir = os.getcwd()

#Making the classes file
classesFile = os.path.join(dir+"/labels", "classes.txt")  
classes = open(classesFile, "a") 
classes.write("fullCircle" + "\n")
classes.write("intersectingCircle" + "\n")
classes.close()
print("Made classes file.")

def makeData(imgID):
    ID = repr(imgID)
    while len(ID) != 6:
        ID = "0" + ID

    circles = []

    startTime = datetime.datetime.now()
    boundingBoxes = []
    imgs = []
    img = r.createImg(height, width)

    #Creating circles
    for i in range(numberOfCircles):
        
        circles.append(c.nonIntersectingCircle(circles, height, width, minRadius, maxRadius))
        boundingBoxes.append(circles[-1].boundingBox(height, width))
        #print(boundingBoxes[-1])
        img = circles[-1].draw(img)

    #Printing how long the circles took to create
    #print("Time taken to make circles: ", datetime.datetime.now() - startTime)

    #r.dispImg(img)

    #Saving the image
    cv2.imwrite(dir+"/images/image_" + ID + ".jpg", img)

    #Saving the bounding boxes to text
    fileName = os.path.join(dir+"/labels", "image_" + ID + ".txt")  
    boxFile = open(fileName,"a") 
    for box in boundingBoxes:
        a = []
        for i in range(1, 5):
            a.append(repr(box[i]))
            while len(a[-1]) != 8:
                a[-1] += "0"
        boxFile.write(repr(box[0]) + " " + a[0] + " " + a[1] + " " + a[2] + " " + a[3] + "\n")

    boxFile.close()
    
for i in range(numImages):
    makeData(i)
    print("Created image " + str(i))
import numpy as np
import sys

class circle():
    def __init__(self, y, x, r, color):
        self.y = y
        self.x = x
        self.r = r
        self.color = color
        
    #draws the circle on the image
    def draw(self, img):
        cR = circleRange(self.y, self.x, self.r)
        for j in range(cR[0][0], cR[0][1]):
            for i in range(cR[1][0], cR[1][1]):
                if j < len(img) and i < len(img[0]) and j >= 0 and i >= 0:
                    if (j - self.y)**2 + (i - self.x)**2 <= self.r**2:
                        img[j][i] = self.color
        return img

    def pixelLocation(self, array):

        cR = circleRange(self.y, self.x, self.r)
        for j in range(cR[0][0], cR[0][1]):
            for i in range(cR[1][0], cR[1][1]):
                if j < len(array) and i < len(array[0]) and j >= 0 and i >= 0:
                    if (j - self.y)**2 + (i - self.x)**2 <= self.r**2:
                        array[j][i] = 1
        return array
        
    #generates the bounding box for the circle
    def boundingBox(self, height, width):
        
        if self.x - self.r < 0:
            widthExcess = True
            if self.x + self.r >= width:
                w = round((width - 1)/width, 6)
                xb = round((1 + width)/(2*width), 6)
            else:
                w = round((self.x + self.r)/width, 6)
                xb = round((1 + self.x + self.r)/(2*width), 6)
        else:
            if self.x + self.r >= width:
                widthExcess = True
                w = round((width - (self.x - self.r))/height, 6)
                xb = round(((self.x - self.r) + width)/(2*width), 6)
            else:
                widthExcess = False
                w = round((2*self.r)/width, 6)
                xb = round((self.x)/(width), 6)
                
        if self.y - self.r < 0:
            heightExcess = True
            if self.y + self.r >= height:
                h = round((height - 1)/height, 6)
                yb = round((1 + height)/(2*height), 6)
            else:
                h = round((self.y + self.r)/height, 6)
                yb = round((1 + self.y + self.r)/(2*height), 6)
        else:
            if self.y + self.r >= height:
                heightExcess = True
                h = round((height - (self.y - self.r))/height, 6)
                yb = round(((self.y - self.r) + height)/(2*height), 6)
            else:
                heightExcess = False
                h = round((2*self.r)/height, 6)
                yb = round((self.y)/(height), 6)
                
        if heightExcess or widthExcess:
            classification = 1
        else:
            classification = 0
        b = [classification, xb, yb, w, h]
        return b
                
#Creates a range of coordinates in which the circle will be drawn
def circleRange(y, x, r):
    return [[y-(r+1), y+(r+1)],[x-(r+1),x+(r+1)]]

#Creates a random circle with bounded parameters
def randomCircle(height, width, minRadius, maxRadius):
    xy = coordinateGen(height, width)
    r = radiusGen(minRadius, maxRadius)
    color = colorGen()
    return circle(xy[0], xy[1], r, color)

#Distance function squared
def distSq(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

#Returns a non-intersecting random circle
def nonIntersectingCircle(circles, height, width, minRadius, maxRadius):
    color = colorGen()
    i = 0
    while i < 100:
        i += 1
        xy = coordinateGen(height, width)
        r = radiusGen(minRadius, maxRadius)
        if len(circles) == 0:
            return circle(xy[0], xy[1], r, color)
        for i in range(len(circles)):
            if distSq(xy, [circles[i].y, circles[i].x]) > (r + circles[i].r)**2:
                if i == len(circles) - 1:
                    #print("Tries taken: " + str(i))
                    return circle(xy[0], xy[1], r, color)
            else:
                break
    print("Exceeded 100 tries to create circle.")
    return
                
#Random coordinate generator
def coordinateGen(height, width):
    v = np.random.rand(2)
    coordinate = [int(v[0]*height), int(v[1]*width)]
    return coordinate

#Random radius generator
def radiusGen(minRadius, maxRadius):
    return np.random.randint(low=minRadius, high=maxRadius, size=1)[0]

#Random color generator
def colorGen():
    color = np.random.rand(3)*255
    return color
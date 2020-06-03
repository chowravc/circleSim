import numpy as np
import random as r
import eulerRotation as eR

class cap():
    
    def __init__(self, x, y, z, color):
        self.x = x
        self.y = y
        self.z = z
        self.color = color
    
# choose radius (of sphere), theta of cap and euler angles
# resolution chooses the number of points
def createCap(theta, radius, angles, resolution, color, forLoops=False):
    # Ratio of surface area of cap to total sphere
    p = 0.5*(1 - np.cos(theta))

    # parametrizing the cap
    if resolution == 0:
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, p*np.pi, 2)
    else:
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, p*np.pi, int(p*resolution))

    # converting to cartesian coordinates
    x = radius * np.outer(np.cos(u), np.sin(v))
    y = radius * np.outer(np.sin(u), np.sin(v))
    z = radius * np.outer(np.ones(np.size(u)), np.cos(v))
    
    # Rotating the cap by euler angles
    if forLoops:
        rotatedCap = eR.rotate(x, y, z, angles)
    else:
        rotatedCap = eR.betterRotate(x, y, z, angles)
    return cap(rotatedCap[0], rotatedCap[1], rotatedCap[2] , color)

def randomCap(radius, resolution):
    # Theta is the variable determining the angular size of these caps on the sphere
    theta = (r.randint(1, 10)+5)*np.pi/100
    
    # Determines the euler angles by which the caps get rotated
    angles = [r.randint(1, 10)*np.pi/5, r.randint(1, 10)*np.pi/5, 0]
    
    # Determines the color of the final island
    color = (r.random(), r.random(), r.random())
    
    # Returning a cap with these parameters
    return createCap(theta, radius, angles, resolution, color)
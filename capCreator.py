import numpy as np
import eulerRotation as eR

#choose radius (of sphere), theta of cap and euler angles
#density chooses the number of points
def cap(theta, radius, angles, resolution):
    #Ratio of surface area of cap to total sphere
    p = 0.5*(1 - np.cos(theta))

    #parametrizing the cap
    if resolution == 0:
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, p*np.pi, 2)
    else:
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, p*np.pi, int(p*resolution))

    #converting to cartesian coordinates
    x = radius * np.outer(np.cos(u), np.sin(v))
    y = radius * np.outer(np.sin(u), np.sin(v))
    z = radius * np.outer(np.ones(np.size(u)), np.cos(v))
    
    #Rotating the cap by euler angles
    xf, yf, zf = eR.rotate(x, y, z, angles)
    
    return xf, yf, zf
import numpy as np
np.seterr(divide='ignore', invalid='ignore')

# Variant of an arctangent function but now with no check
def atan2(y, x):
    var = (y/np.sqrt(x**2 + y**2) - x)
    return 2*np.arctan(var)

# Finds the x coordinates
def laeax(lat, long):
    x = (2*np.sqrt(2)*np.cos(lat)*np.sin(long/2))/np.sqrt(1 + np.cos(lat)*np.cos(long/2))
    return x

# Finds the y coordinates
def laeay(lat, long):
    y =  (np.sqrt(2)*np.sin(lat))/np.sqrt(1 + np.cos(lat)*np.cos(long/2))
    return y

# Converts cartesian to geographic
def geographic(xf, yf, zf, radius): # FASTER AND BETTER BUT GIVES DIVIDE BY ZERO ERRORS
    lats = np.arcsin(zf/radius)
    longs = atan2(yf, xf)
    
    return lats, longs

# Projects an arbitrary object
def project(xf, yf, zf, color, radius): # FASTER AND BETTER BUT GIVES ERRORS
    
    lats, longs = geographic(xf, yf, zf, radius)
    xh = laeax(lats, longs)
    yh = laeay(lats, longs)
    
    return xh, yh, color

# Projects cap object
def projectCap(cap, radius):
    return project(cap.x, cap.y, cap.z, cap.color, radius)
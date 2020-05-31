import numpy as np

# Calculates Rotation Matrix given euler angles.
def createRotation(theta):
    R_x = np.array([[1, 0, 0],
                    [0, np.cos(theta[0]), -np.sin(theta[0])],
                    [0, np.sin(theta[0]), np.cos(theta[0])]])
                    
    R_y = np.array([[np.cos(theta[1]), 0, np.sin(theta[1])],
                    [0, 1, 0],
                    [-np.sin(theta[1]), 0, np.cos(theta[1])]])
                    
    R_z = np.array([[np.cos(theta[2]), -np.sin(theta[2]), 0],
                    [np.sin(theta[2]), np.cos(theta[2]), 0],
                    [0, 0, 1]])
                    
    R = np.dot(R_z, np.dot(R_y, R_x ))
    return R

# Rotates an object as arrays of x, y and z using euler angles theta, a list of 3 angles.
def rotate(x, y, z, theta):
    R = createRotation(theta)
    xf = []
    yf = []
    zf = []

    #Creating lists of xs, ys and zs
    for ite in range(len(x)):
        xs = x[ite]
        ys = y[ite]
        zs = z[ite]
    
        points = []
        for jte in range(len(xs)):
            points.append([xs[jte], ys[jte], zs[jte]])
        
        rotatedPoints = np.dot(points, R)
    
        xr = []
        yr = []
        zr = []
    
        for point in rotatedPoints:
            xr.append(point[0])
            yr.append(point[1])
            zr.append(point[2])
    
        xf.append(xr)
        yf.append(yr)
        zf.append(zr)

    xf = np.asarray(xf)
    yf = np.asarray(yf)
    zf = np.asarray(zf)
    
    return xf, yf, zf
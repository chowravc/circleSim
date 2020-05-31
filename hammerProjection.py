import numpy as np

def atan2(y, x):
    if x**2 + y**2 == 0:
        return np.pi
    else:
        var = (y/np.sqrt(x**2 + y**2) - x)
        return 2*np.arctan(var)
    
def laeax(lat, long):
    x = (2*np.sqrt(2)*np.cos(lat)*np.sin(long/2))/np.sqrt(1 + np.cos(lat)*np.cos(long/2))
    return x
    
def laeay(lat, long):
    y =  (np.sqrt(2)*np.sin(lat))/np.sqrt(1 + np.cos(lat)*np.cos(long/2))
    return y

def geographic(xf, yf, zf, radius):
    lats = []
    longs = []

    for ite in range(len(xf)):
        sublat = []
        sublong = []
        for jte in range(len(xf[0])):
            sublat.append(np.arcsin(zf[ite][jte]/radius))
            sublong.append(atan2(yf[ite][jte], xf[ite][jte]))
            #if xf[ite][jte] == 0:
                #sublong.append(np.pi/2)
            #else:
                #sublong.append(np.arctan(yf[ite][jte]/xf[ite][jte]))
        lats.append(sublat)
        longs.append(sublong)
        
    return lats, longs
    
def project(xf, yf, zf, radius):
    lats, longs = geographic(xf, yf, zf, radius)
    xh = []
    yh = []

    for ite in range(len(lats)):
        subxh = []
        subyh = []
        for jte in range(len(lats[0])):
            subxh.append(laeax(lats[ite][jte], longs[ite][jte]))
            subyh.append(laeay(lats[ite][jte], longs[ite][jte]))
        xh.append(subxh)
        yh.append(subyh)
    
    return xh, yh
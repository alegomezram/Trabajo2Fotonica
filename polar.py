import numpy as np

def car_polar(x,y):
    r = np.sqrt((x ** 2) + (y ** 2))
    theta = np.arctan(y/x)
    return (r, theta)


def polar_car(r,theta):
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    return (x,y)
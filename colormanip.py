"""
Various functions to help with manipulating colors
"""
import Line
import c_mathhelp as mathhelp
import random
import time
from math import floor, sin

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

def getShade(triangle, ray, intersection):
    ray = mathhelp.normalize(Line.Line(ray.start, intersection).vectorize())
    trinorm = mathhelp.normalize(triangle.normal())
    dot = mathhelp.dotproduct(ray, trinorm)
    return (0.3 + (0.7 * abs(dot)))


def randomColor():
    return(random.randint(0,255),
           random.randint(0,255),
           random.randint(0,255))

def randomColorTimeBased():
    # s = 32
    # colorbase = s * s
    # n = (time.time() * 10) % colorbase

    # p = floor(n / (s * s))
    # r = floor((n - (s * s * p)) / s)
    # c = floor((n - (s * s * p)) - (r * s))

    # red = (255 / s) * p
    # green = (255 / s) * r
    # blue = (255 / s) * c

    # return (red, green, blue)

    t = time.time() / 10

    red =   (((sin(t + 0)) + 1) / 2) * 255
    green = (((sin(t + 2)) + 1) / 2) * 255
    blue =  (((sin(t + 4)) + 1) / 2) * 255
    
    return (red, green, blue)
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


reverseColorValueMap = {
    BLACK: "BLACK",
    WHITE: "WHITE",
    GRAY: "GRAY",
    RED: "RED",
    GREEN: "GREEN",
    BLUE: "BLUE",
    YELLOW: "YELLOW",
    CYAN: "CYAN",
    MAGENTA: "MAGENTA"
}

def getClosestColorName(inColor):
    """Returns color string that's closest to the input color"""
    def rgb_diff(color1, color2):
        tot_diff = 0
        for i in range(0, 3):
            tot_diff += abs(color1[i] - color2[i])
        return tot_diff

    min_diff = 1000
    min_diff_color = BLACK

    for testColor in [BLACK, WHITE, GRAY, RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA]:
        diff = rgb_diff(inColor, testColor)
        if diff < min_diff:
            min_diff = diff
            min_diff_color = testColor

    return reverseColorValueMap[min_diff_color]

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
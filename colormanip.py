import Line
import c_mathhelp as mathhelp
import random

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
import math
import Line

def dotproduct(p1, p2):
    return (p1[0] * p2[0]) + \
           (p1[1] * p2[1]) + \
           (p1[2] * p2[2])

def magnitude(p1):
    return math.sqrt((p1[0] ** 2) +
                     (p1[1] ** 2) + 
                     (p1[2] ** 2))

def angleBetweenLines(p1, p2):
    top = dotproduct(p1, p2)
    bottom = magnitude(p1) * magnitude(p2)
    if areEqualFloats(top, bottom):
        return 0
    else:
        try:
            return math.acos(top/bottom)
        except ValueError as e:
            print("Something is wonky with the numbers you're trying to acos")
            print(str(top))
            print(str(bottom))
            print(e)
            exit()

def subtractPoint(left, right):
    #left - right
    x = left[0] - right[0]
    y = left[1] - right[1]
    z = left[2] - right[2]

    return(x, y, z)

def areEqualFloats(f1, f2):
    avg = (f1 + f2) / 2.0
    epsilon = avg * 0.000001

    if abs(f1-f2) < epsilon:
        return True
    else:
        return False

def normalize(p1):
    mag = magnitude(p1)
    x = p1[0] / mag
    y = p1[1] / mag
    z = p1[2] / mag
    
    return (x, y, z)
        
def cross(p1, p2):
    x = (p1[1] * p2[2]) - (p1[2] * p2[1])
    y = (p1[2] * p2[0]) - (p1[0] * p2[2])
    z = (p1[0] * p2[1]) - (p1[1] * p2[0])
    return (x, y, z)

def distanceFromPointToLine(point, line):
    #normalize point and line to start of line
    normLine = line.normalize()
    normPoint = Line.Line(line.start, point).normalize()
    #calculate angle between lines
    a = angleBetweenLines(normLine, normPoint)
    #calculate distance from start of line to point (hypotenuse)
    H = magnitude(normPoint)
    return math.sin(a) * H

def lineImpactsSphere(sphere, line):
    dist = distanceFromPointToLine(sphere.center, line)
    return dist < sphere.rad    
    
def triangleLineIntersect(triangle, line):
    #figure out the normal of the triangle's plane
    n = normalize(triangle.normal())
    d = dotproduct(n, triangle.A)
    
    return d
    
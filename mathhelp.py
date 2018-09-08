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
    return (x, y, z)

def addPoint(left, right):
    x = left[0] + right[0]
    y = left[1] + right[1]
    z = left[2] + right[2]
    return (x, y, z)

def multiplyPointByScalar(p1, scalar):
    x = p1[0] * scalar
    y = p1[1] * scalar
    z = p1[2] * scalar
    return (x, y, z)

def areEqualFloats(f1, f2):
    # print('Comparing numbers:')
    # print(f1)
    # print(f1)
    # print('----')
    avg = (f1 + f2) / 2.0
    if avg < 0.0001:
        avg = 1
    epsilon = avg * 0.000000001

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
    normLine = line.vectorize()
    normPoint = Line.Line(line.start, point).vectorize()
    #calculate angle between lines
    a = angleBetweenLines(normLine, normPoint)
    #calculate distance from start of line to point (hypotenuse)
    H = magnitude(normPoint)
    return math.sin(a) * H

def lineImpactsSphere(sphere, line):
    dist = distanceFromPointToLine(sphere.center, line)
    return dist < sphere.rad

def triangleLineIntersect(triangle, line):
    # Based on handout by Brian Curless:
    # https://courses.cs.washington.edu/courses/csep557/10au/lectures/triangle_intersection.pdf

    #figure out the normal of the triangle's plane
    n = normalize(triangle.normal())
    #find p (line origin) and dir (line direction vector)
    P = line.start
    dir = normalize(line.vectorize())

    #solve for d (righthand of plane equation)
    d = dotproduct(n, triangle.A)
    #solve for t : vector magnitude coeficcient in ray equation
    #             R(t) = P + t * dir
    top = d - dotproduct(n, P)
    bottom = dotproduct(n, dir)
    #if the bottom is 0, the line is parallel to the triangle
    #(triangle normal and dir are perpendicular)
    if areEqualFloats(bottom, 0.0):
        print('Triangle and line are perpendicular')
        return None
    t =  top / bottom
    # plug T into the equation for the ray to get ray-plane intersection
    Q = addPoint(P, multiplyPointByScalar(dir, t))
    #figure out whether the point is inside the triangle or not
    # by checking if it's 'to the right' of all the triangle's edges
    AB = Line.Line(triangle.A, triangle.B).vectorize()
    AQ = Line.Line(triangle.A, Q).vectorize()
    ABcross = dotproduct(cross(AB, AQ), n)
    if ABcross < 0:
        return None
    BC = Line.Line(triangle.B, triangle.C).vectorize()
    BQ = Line.Line(triangle.B, Q).vectorize()
    BCcross = dotproduct(cross(BC, BQ), n)
    if BCcross < 0:
        return None
    CA = Line.Line(triangle.C, triangle.A).vectorize()
    CQ = Line.Line(triangle.C, Q).vectorize()
    CAcross = dotproduct(cross(CA, CQ), n)
    if CAcross < 0:
        return None
    return Q

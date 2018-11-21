import math
import Line
import c_mathhelp


def angleBetweenLines(p1, p2):
    top = c_mathhelp.dotproduct(p1, p2)
    bottom = c_mathhelp.magnitude(p1) * c_mathhelp.magnitude(p2)
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

def areEqualFloats(f1, f2):
    avg = (f1 + f2) / 2.0
    if avg < 0.0001:
        avg = 1
    epsilon = avg * 0.000000001

    if abs(f1-f2) < epsilon:
        return True
    else:
        return False

# V2
def cross(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    x = (y1 * z2) - (z1 * y2)
    y = (z1 * x2) - (x1 * z2)
    z = (x1 * y2) - (y1 * x2)
    return (x, y, z)

def distanceFromPointToLine(point, line):
    #normalize point and line to start of line
    normLine = line.vectorize()
    normPoint = Line.Line(line.start, point).vectorize()
    #calculate angle between lines
    a = angleBetweenLines(normLine, normPoint)
    #calculate distance from start of line to point (hypotenuse)
    H = c_mathhelp.magnitude(normPoint)
    return math.sin(a) * H

def lineImpactsSphere(sphere, line):
    dist = distanceFromPointToLine(sphere.center, line)
    return dist < sphere.rad

# # V3
def triangleLineIntersect(triangle, line):
    # Based on handout by Brian Curless:
    # https://courses.cs.washington.edu/courses/csep557/10au/lectures/triangle_intersection.pdf
    #print(triangle)
    #figure out the normal of the triangle's plane
    tA = triangle.A
    tB = triangle.B
    tC = triangle.C
    n = c_mathhelp.normalize(triangle.normal())
    #find p (line origin) and dirv (line direction vector)
    P = line.start
    end = line.end
    dirv = c_mathhelp.normalize(c_mathhelp.subtractPoint(P, end))
    #solve for d (righthand of plane equation)
    d = c_mathhelp.dotproduct(n, tA)
    #solve for t : vector magnitude coeficcient in ray equation
    #             R(t) = P + t * dirv
    top = d - c_mathhelp.dotproduct(n, P)
    bottom = c_mathhelp.dotproduct(n, dirv)
    #if the bottom is 0, the line is parallel to the triangle
    #(triangle normal and dirv are perpendicular)
    if areEqualFloats(bottom, 0.0):
        return None
    t =  top / bottom
    # plug T into the equation for the ray to get ray-plane intersection
    Q = c_mathhelp.addPoint(P, c_mathhelp.multiplyPointByScalar(dirv, t))
    #If the intersection is behind the screen, ignore it
    #figure out whether the point is inside the triangle or not
    # by checking if it's 'to the right' of all the triangle's edges
    AB = c_mathhelp.subtractPoint(tB, tA)
    AQ = c_mathhelp.subtractPoint(Q, tA)
    ABcross = c_mathhelp.dotproduct(cross(AB, AQ), n)
    if ABcross < 0:
        return None
    BC = c_mathhelp.subtractPoint(tC, tB)
    BQ = c_mathhelp.subtractPoint(Q, tB)
    BCcross = c_mathhelp.dotproduct(cross(BC, BQ), n)
    if BCcross < 0:
        return None
    CA = c_mathhelp.subtractPoint(tA, tC)
    CQ = c_mathhelp.subtractPoint(Q, tC)
    CAcross = c_mathhelp.dotproduct(cross(CA, CQ), n)
    if CAcross < 0:
        return None
    return Q
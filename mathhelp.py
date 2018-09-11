import math
import Line

# # V1
# def dotproduct(p1, p2):
#     return (p1[0] * p2[0]) + \
#            (p1[1] * p2[1]) + \
#            (p1[2] * p2[2])

# # V2
def dotproduct(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return (x1 * x2) + \
           (y1 * y2) + \
           (z1 * z2)

# V1
# def magnitude(p1):
#    return math.sqrt((p1[0] ** 2) +
#                     (p1[1] ** 2) +
#                     (p1[2] ** 2))

# V2
def magnitude(p1):
    px, py, pz = p1
    return math.sqrt((px * px) + 
                     (py * py) +
                     (pz * pz))

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

# V1
# def subtractPoint(left, right):
#     #left - right
#     x = left[0] - right[0]
#     y = left[1] - right[1]
#     z = left[2] - right[2]
#     return (x, y, z)

# V2
def subtractPoint(left, right):
    lx, ly, lz = left
    rx, ry, rz = right
    return (lx - rx, ly - ry, lz - rz)

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

# # V1
# def cross(p1, p2):
#     x = (p1[1] * p2[2]) - (p1[2] * p2[1])
#     y = (p1[2] * p2[0]) - (p1[0] * p2[2])
#     z = (p1[0] * p2[1]) - (p1[1] * p2[0])
#     return (x, y, z)

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
    H = magnitude(normPoint)
    return math.sin(a) * H

def lineImpactsSphere(sphere, line):
    dist = distanceFromPointToLine(sphere.center, line)
    return dist < sphere.rad

# #V1
# def triangleLineIntersect(triangle, line):
#     # Based on handout by Brian Curless:
#     # https://courses.cs.washington.edu/courses/csep557/10au/lectures/triangle_intersection.pdf
#     #print(triangle)
#     #figure out the normal of the triangle's plane
#     n = normalize(triangle.normal())
#     #find p (line origin) and dirv (line direction vector)
#     P = line.start
#     dirv = normalize(line.vectorize())
#     #solve for d (righthand of plane equation)
#     d = dotproduct(n, triangle.A)
#     #solve for t : vector magnitude coeficcient in ray equation
#     #             R(t) = P + t * dirv
#     top = d - dotproduct(n, P)
#     bottom = dotproduct(n, dirv)
#     #if the bottom is 0, the line is parallel to the triangle
#     #(triangle normal and dirv are perpendicular)
#     if areEqualFloats(bottom, 0.0):
#         return None
#     t =  top / bottom
#     # plug T into the equation for the ray to get ray-plane intersection
#     Q = addPoint(P, multiplyPointByScalar(dirv, t))
#     #If the intersection is behind the screen, ignore it
#     #figure out whether the point is inside the triangle or not
#     # by checking if it's 'to the right' of all the triangle's edges
#     AB = Line.Line(triangle.A, triangle.B).vectorize()
#     AQ = Line.Line(triangle.A, Q).vectorize()
#     ABcross = dotproduct(cross(AB, AQ), n)
#     if ABcross < 0:
#         return None
#     BC = Line.Line(triangle.B, triangle.C).vectorize()
#     BQ = Line.Line(triangle.B, Q).vectorize()
#     BCcross = dotproduct(cross(BC, BQ), n)
#     if BCcross < 0:
#         return None
#     CA = Line.Line(triangle.C, triangle.A).vectorize()
#     CQ = Line.Line(triangle.C, Q).vectorize()
#     CAcross = dotproduct(cross(CA, CQ), n)
#     if CAcross < 0:
#         return None
#     return Q


# #V2
# def triangleLineIntersect(triangle, line):
#     # Based on handout by Brian Curless:
#     # https://courses.cs.washington.edu/courses/csep557/10au/lectures/triangle_intersection.pdf
#     #print(triangle)
#     #figure out the normal of the triangle's plane
#     n = normalize(triangle.normal())
#     #find p (line origin) and dirv (line direction vector)
#     P = line.start
#     end = line.end
#     dirv = normalize(subtractPoint(P, end))
#     #solve for d (righthand of plane equation)
#     d = dotproduct(n, triangle.A)
#     #solve for t : vector magnitude coeficcient in ray equation
#     #             R(t) = P + t * dirv
#     top = d - dotproduct(n, P)
#     bottom = dotproduct(n, dirv)
#     #if the bottom is 0, the line is parallel to the triangle
#     #(triangle normal and dirv are perpendicular)
#     if areEqualFloats(bottom, 0.0):
#         return None
#     t =  top / bottom
#     # plug T into the equation for the ray to get ray-plane intersection
#     Q = addPoint(P, multiplyPointByScalar(dirv, t))
#     #If the intersection is behind the screen, ignore it
#     #figure out whether the point is inside the triangle or not
#     # by checking if it's 'to the right' of all the triangle's edges
#     AB = subtractPoint(triangle.B, triangle.A)
#     AQ = subtractPoint(Q, triangle.A)
#     ABcross = dotproduct(cross(AB, AQ), n)
#     if ABcross < 0:
#         return None
#     BC = subtractPoint(triangle.C, triangle.B)
#     BQ = subtractPoint(Q, triangle.B)
#     BCcross = dotproduct(cross(BC, BQ), n)
#     if BCcross < 0:
#         return None
#     CA = subtractPoint(triangle.A, triangle.C)
#     CQ = subtractPoint(Q, triangle.C)
#     CAcross = dotproduct(cross(CA, CQ), n)
#     if CAcross < 0:
#         return None
#     return Q

# V3
def triangleLineIntersect(triangle, line):
    # Based on handout by Brian Curless:
    # https://courses.cs.washington.edu/courses/csep557/10au/lectures/triangle_intersection.pdf
    #print(triangle)
    #figure out the normal of the triangle's plane
    tA = triangle.A
    tB = triangle.B
    tC = triangle.C
    n = normalize(triangle.normal())
    #find p (line origin) and dirv (line direction vector)
    P = line.start
    end = line.end
    dirv = normalize(subtractPoint(P, end))
    #solve for d (righthand of plane equation)
    d = dotproduct(n, tA)
    #solve for t : vector magnitude coeficcient in ray equation
    #             R(t) = P + t * dirv
    top = d - dotproduct(n, P)
    bottom = dotproduct(n, dirv)
    #if the bottom is 0, the line is parallel to the triangle
    #(triangle normal and dirv are perpendicular)
    if areEqualFloats(bottom, 0.0):
        return None
    t =  top / bottom
    # plug T into the equation for the ray to get ray-plane intersection
    Q = addPoint(P, multiplyPointByScalar(dirv, t))
    #If the intersection is behind the screen, ignore it
    #figure out whether the point is inside the triangle or not
    # by checking if it's 'to the right' of all the triangle's edges
    AB = subtractPoint(tB, tA)
    AQ = subtractPoint(Q, tA)
    ABcross = dotproduct(cross(AB, AQ), n)
    if ABcross < 0:
        return None
    BC = subtractPoint(tC, tB)
    BQ = subtractPoint(Q, tB)
    BCcross = dotproduct(cross(BC, BQ), n)
    if BCcross < 0:
        return None
    CA = subtractPoint(tA, tC)
    CQ = subtractPoint(Q, tC)
    CAcross = dotproduct(cross(CA, CQ), n)
    if CAcross < 0:
        return None
    return Q
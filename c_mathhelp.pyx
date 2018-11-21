"""
Various Cython math functions
Prefer to use these over the equivalents in mathhelp.py, they are much faster
"""
def dotproduct((float, float, float) p1, (float, float, float) p2):
    cdef float result
    result = (p1[0] * p2[0]) + (p1[1] * p2[1]) + (p1[2] * p2[2])
    return result

cdef float c_dotproduct((float, float, float) p1, (float, float, float) p2):
    cdef float result
    result = (p1[0] * p2[0]) + (p1[1] * p2[1]) + (p1[2] * p2[2])
    return result

def magnitude((float, float, float) p1):
    x = p1[0]
    y = p1[1]
    z = p1[2]
    return ((x*x) + (y*y) + (z*z)) ** (0.5)

def subtractPoint((float, float, float) left, (float, float, float) right):
    cdef (float, float, float) result
    result[0] = left[0] - right[0]
    result[1] = left[1] - right[1]
    result[2] = left[2] - right[2]
    return result

cdef (float, float, float) c_subtractPoint((float, float, float) left, (float, float, float) right):
    cdef (float, float, float) result
    result[0] = left[0] - right[0]
    result[1] = left[1] - right[1]
    result[2] = left[2] - right[2]
    return result

def addPoint((float, float, float) left, (float, float, float) right):
    cdef (float, float, float) result
    result = (0, 0, 0)
    result[0] = left[0] + right[0]
    result[1] = left[1] + right[1]
    result[2] = left[2] + right[2]
    return result

cdef (float, float, float) c_addPoint((float, float, float) left, (float, float, float) right):
    cdef (float, float, float) result
    result = (0, 0, 0)
    result[0] = left[0] + right[0]
    result[1] = left[1] + right[1]
    result[2] = left[2] + right[2]
    return result

def multiplyPointByScalar((float, float, float) p1, float scalar):
    cdef (float, float, float) result
    result[0] = p1[0] * scalar
    result[1] = p1[1] * scalar
    result[2] = p1[2] * scalar
    return result

cdef (float, float, float) c_multiplyPointByScalar((float, float, float) p1, float scalar):
    cdef (float, float, float) result
    result[0] = p1[0] * scalar
    result[1] = p1[1] * scalar
    result[2] = p1[2] * scalar
    return result

def normalize((float, float, float) p1):
    cdef (float, float, float) result
    mag = magnitude(p1)
    result[0] = p1[0] / mag
    result[1] = p1[1] / mag
    result[2] = p1[2] / mag
    return result

cdef (float, float, float) c_normalize((float, float, float) p1):
    cdef (float, float, float) result
    mag = magnitude(p1)
    result[0] = p1[0] / mag
    result[1] = p1[1] / mag
    result[2] = p1[2] / mag
    return result

def cross((float, float, float) p1, (float, float, float) p2):
    cdef (float, float, float) result
    result[0] = (p1[1] * p2[2]) - (p1[2] * p2[1])
    result[1] = (p1[2] * p2[0]) - (p1[0] * p2[2])
    result[2] = (p1[0] * p2[1]) - (p1[1] * p2[0])
    return result

cdef (float, float, float) c_cross((float, float, float) p1, (float, float, float) p2):
    cdef (float, float, float) result
    result[0] = (p1[1] * p2[2]) - (p1[2] * p2[1])
    result[1] = (p1[2] * p2[0]) - (p1[0] * p2[2])
    result[2] = (p1[0] * p2[1]) - (p1[1] * p2[0])
    return result

def triangleLineIntersect((float, float, float) tA, 
                          (float, float, float) tB,
                          (float, float, float) tC,
                          (float, float, float) lineStart,
                          (float, float, float) lineEnd):

    #get triangle normal n
    cdef (float, float, float) p1 = c_subtractPoint(tB, tA)
    cdef (float, float, float) p2 = c_subtractPoint(tC, tA)
    cdef (float, float, float) n = c_cross(p1, p2)
    n = c_normalize(n)

    #find line origin P and line direction dirv
    cdef (float, float, float) P = lineStart
    cdef (float, float, float) end = lineEnd
    cdef (float, float, float) dirv = c_subtractPoint(P, end)
    dirv = c_normalize(dirv)

    #solve for d (righthand of plane equation)
    cdef float d = c_dotproduct(n, tA)

    #solve for t
    cdef float top = d - c_dotproduct(n, P)
    cdef float bottom = c_dotproduct(n, dirv)
    if bottom < 0.000001 and bottom > -0.000001:
        return None
    t = top / bottom

    #find Q (plane-line intersection)
    dirv_t = c_multiplyPointByScalar(dirv, t)
    cdef (float, float, float) Q = c_addPoint(P, dirv_t)
    
    #find whether Q is inside the triangle
    cdef (float, float, float) AB = c_subtractPoint(tB, tA)
    cdef (float, float, float) AQ = c_subtractPoint(Q, tA)
    cdef float ABCross = c_dotproduct(c_cross(AB, AQ), n)
    if ABCross < 0:
        return None

    cdef (float, float, float) BC = c_subtractPoint(tC, tB)
    cdef (float, float, float) BQ = c_subtractPoint(Q, tB)
    cdef float BCCross = c_dotproduct(c_cross(BC, BQ), n)
    if BCCross < 0:
        return None
        
    cdef (float, float, float) CA = c_subtractPoint(tA, tC)
    cdef (float, float, float) CQ = c_subtractPoint(Q, tC)
    cdef float CACross = c_dotproduct(c_cross(CA, CQ), n)
    if CACross < 0:
        return None
    return Q


cdef (float, float, float) c_triangleLineIntersect((float, float, float) tA, 
                          (float, float, float) tB,
                          (float, float, float) tC,
                          (float, float, float) lineStart,
                          (float, float, float) lineEnd):

    #get triangle normal n
    cdef (float, float, float) p1 = c_subtractPoint(tB, tA)
    cdef (float, float, float) p2 = c_subtractPoint(tC, tA)
    cdef (float, float, float) n = c_cross(p1, p2)
    n = c_normalize(n)

    #find line origin P and line direction dirv
    cdef (float, float, float) P = lineStart
    cdef (float, float, float) end = lineEnd
    cdef (float, float, float) dirv = c_subtractPoint(P, end)
    dirv = c_normalize(dirv)

    #solve for d (righthand of plane equation)
    cdef float d = c_dotproduct(n, tA)

    #solve for t
    cdef float top = d - c_dotproduct(n, P)
    cdef float bottom = c_dotproduct(n, dirv)
    if bottom < 0.000001 and bottom > -0.000001:
        return (0, 0, -1)
    t = top / bottom

    #find Q (plane-line intersection)
    dirv_t = c_multiplyPointByScalar(dirv, t)
    cdef (float, float, float) Q = c_addPoint(P, dirv_t)
    
    #find whether Q is inside the triangle
    cdef (float, float, float) AB = c_subtractPoint(tB, tA)
    cdef (float, float, float) AQ = c_subtractPoint(Q, tA)
    cdef float ABCross = c_dotproduct(c_cross(AB, AQ), n)
    if ABCross < 0:
        return (-1, -1, -1)

    cdef (float, float, float) BC = c_subtractPoint(tC, tB)
    cdef (float, float, float) BQ = c_subtractPoint(Q, tB)
    cdef float BCCross = c_dotproduct(c_cross(BC, BQ), n)
    if BCCross < 0:
        return (-1, -1, -1)
        
    cdef (float, float, float) CA = c_subtractPoint(tA, tC)
    cdef (float, float, float) CQ = c_subtractPoint(Q, tC)
    cdef float CACross = c_dotproduct(c_cross(CA, CQ), n)
    if CACross < 0:
        return (-1, -1, -1)
    return Q

def castRay(ray, tris, numTris):
    cdef float nearestIntersectionZ = 1000000000
    cdef (int, int, int) nearestIntersectionColor = (0, 0, 0)
    cdef float dot, shade
    cdef float R, G, B
    cdef (float, float, float) intersection, rayd, trinorm
    for triangleIdx in range(0, numTris):
        triangle = tris[triangleIdx]
        intersection =  c_triangleLineIntersect(triangle.A, triangle.B, triangle.C, ray.start, ray.end)

        if intersection != (-1, -1, -1) and intersection[2] > 0.0 and intersection[2] < nearestIntersectionZ:
                    nearestIntersectionZ = intersection[2]
                    rayd = c_normalize(c_subtractPoint(intersection, ray.start))
                    trinorm = c_normalize(triangle.normal())
                    dot = c_dotproduct(rayd, trinorm)
                    shade =  (0.3 + (0.7 * abs(dot)))
                    R = triangle.color[0] * shade
                    G = triangle.color[1] * shade
                    B = triangle.color[2] * shade
                    nearestIntersectionColor = (<int>R, <int>G, <int>B)
    return nearestIntersectionColor 

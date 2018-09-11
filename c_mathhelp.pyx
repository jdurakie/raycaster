def dotproduct((float, float, float) p1, (float, float, float) p2):
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

def addPoint((float, float, float) left, (float, float, float) right):
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

def normalize((float, float, float) p1):
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

def triangleLineIntersect((float, float, float) tA, 
                          (float, float, float) tB,
                          (float, float, float) tC,
                          (float, float, float) lineStart,
                          (float, float, float) lineEnd):

    #get triangle normal n
    cdef (float, float, float) p1 = subtractPoint(tB, tA)
    cdef (float, float, float) p2 = subtractPoint(tC, tA)
    cdef (float, float, float) n = cross(p1, p2)
    n = normalize(n)

    #find line origin P and line direction dirv
    cdef (float, float, float) P = lineStart
    cdef (float, float, float) end = lineEnd
    cdef (float, float, float) dirv = subtractPoint(P, end)
    dirv = normalize(dirv)

    #solve for d (righthand of plane equation)
    cdef float d = dotproduct(n, tA)

    #solve for t
    cdef float top = d - dotproduct(n, P)
    cdef float bottom = dotproduct(n, dirv)
    if bottom < 0.000001 and bottom > -0.000001:
        return None
    t = top / bottom

    #find Q (plane-line intersection)
    dirv_t = multiplyPointByScalar(dirv, t)
    cdef (float, float, float) Q = addPoint(P, dirv_t)
    
    #find whether Q is inside the triangle
    cdef (float, float, float) AB = subtractPoint(tB, tA)
    cdef (float, float, float) AQ = subtractPoint(Q, tA)
    cdef float ABCross = dotproduct(cross(AB, AQ), n)
    if ABCross < 0:
        return None

    cdef (float, float, float) BC = subtractPoint(tC, tB)
    cdef (float, float, float) BQ = subtractPoint(Q, tB)
    cdef float BCCross = dotproduct(cross(BC, BQ), n)
    if BCCross < 0:
        return None
        
    cdef (float, float, float) CA = subtractPoint(tA, tC)
    cdef (float, float, float) CQ = subtractPoint(Q, tC)
    cdef float CACross = dotproduct(cross(CA, CQ), n)
    if CACross < 0:
        return None
    return Q
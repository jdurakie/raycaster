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
    result = (0, 0, 0)
    result[0] = left[0] - right[0]
    result[1] = left[1] - right[1]
    result[2] = left[2] - right[2]
    return result

def addtPoint((float, float, float) left, (float, float, float) right):
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

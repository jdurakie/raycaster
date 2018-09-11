from math import sin, cos
import mathhelp
import Triangle

def applyRotationMatrix(p1, R):
    x = sum([p1[0] * R[0][0], p1[1] * R[1][0], p1[2] * R[2][0]])
    y = sum([p1[0] * R[0][1], p1[1] * R[1][1], p1[2] * R[2][1]])
    z = sum([p1[0] * R[0][2], p1[1] * R[1][2], p1[2] * R[2][2]])
    return (x, y, z)
    
def rotatePointAroundX(p1, theta):
    Rx = [[1,          0,             0],
          [0, cos(theta), -1*sin(theta)],
          [0, sin(theta),    cos(theta)]]
    return applyRotationMatrix(p1, Rx)

def rotatePointAroundY(p1, theta):
    Ry = [[   cos(theta), 0, sin(theta)],
          [            0, 1,          0],
          [-1*sin(theta), 0, cos(theta)]]
    return applyRotationMatrix(p1, Ry)

def rotatePointAroundZ(p1, theta):
    Rz = [[cos(theta), -1*sin(theta), 0],
          [sin(theta),    cos(theta), 0],
          [         0,             0, 1]]
    return applyRotationMatrix(p1, Rz)

def rotatePointAroundPointInX(p1, p2, theta):
    translatedPoint = mathhelp.subtractPoint(p1, p2)
    translatedPoint = rotatePointAroundX(translatedPoint, theta)    
    #un-translate the point
    return mathhelp.addPoint(translatedPoint, p2)

def rotatePointAroundPointInY(p1, p2, theta):
    translatedPoint = mathhelp.subtractPoint(p1, p2)
    translatedPoint = rotatePointAroundY(translatedPoint, theta)    
    #un-translate the point
    return mathhelp.addPoint(translatedPoint, p2)

def rotatePointAroundPointInZ(p1, p2, theta):
    translatedPoint = mathhelp.subtractPoint(p1, p2)
    translatedPoint = rotatePointAroundZ(translatedPoint, theta)
    #un-translate the point
    return mathhelp.addPoint(translatedPoint, p2)

def rotateTrisAroundCentroidInX(tris, theta):
    pointSum = (0, 0, 0)
    for tri in tris:
        pointSum = mathhelp.addPoint(pointSum, tri.centroid())
    center = mathhelp.multiplyPointByScalar(pointSum, 1.0 / len(tris))
    for tri in tris:
        tri.rotateAroundPointInX(center, theta)

def rotateTrisAroundPointInY(tris, theta, p1):
    for tri in tris:
        tri.rotateAroundPointInY(p1, theta)
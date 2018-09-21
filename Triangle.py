#TRIANGLES DEFINED COUNTER-CLOCK WISE:
#     C
#    / \
#   /   \
#  /     \
# A-------B

import c_mathhelp
import rotations
import mathhelp
import c_mathhelp

class Triangle(object):
    """
    Contains the three points of a triangle.
    """
    def __init__(self, A, B, C, color=(0,255,0), id=0):
        """
        A, B, C: tuples with (x, y, z) coords
        color: tuple with RGB color (0-255, 0-255, 0-255)
        id: if you want to, you can give this triangle an ID number
        """
        self.A = A
        self.B = B
        self.C = C
        self.color = color
        self.id = id

    def __repr__(self):
        coords = str(self.A) + ',' + str(self.B) + ',' + str(self.C) + '\n'
        norm = 'Normal: ' + str(self.normal()) 
        return coords + norm

    def centroid(self):
        """
        Calculates the centroid of the triangle
        """
        pointSum = c_mathhelp.addPoint(self.A, c_mathhelp.addPoint(self.B, self.C))
        return c_mathhelp.multiplyPointByScalar(pointSum, 1.0/3.0)

    def normal(self):
        """
        Calculates the normal vector of the triangle
        """
        p1 = c_mathhelp.subtractPoint(self.B, self.A)
        p2 = c_mathhelp.subtractPoint(self.C, self.A)
        return mathhelp.cross(p1, p2)

    def rotateAroundX(self, theta):
        """
        Rotates around X axis
        theta: rotation angle in radians
        """
        self.A = rotations.rotatePointAroundX(self.A, theta)
        self.B = rotations.rotatePointAroundX(self.B, theta)
        self.C = rotations.rotatePointAroundX(self.C, theta)

    def rotateAroundY(self, theta):
        """
        Rotates around Y axis
        theta: rotation angle in radians
        """
        self.A = rotations.rotatePointAroundY(self.A, theta)
        self.B = rotations.rotatePointAroundY(self.B, theta)
        self.C = rotations.rotatePointAroundY(self.C, theta)

    def rotateAroundZ(self, theta):
        """
        Rotates around Z axis
        theta: rotation angle in radians
        """
        self.A = rotations.rotatePointAroundZ(self.A, theta)
        self.B = rotations.rotatePointAroundZ(self.B, theta)
        self.C = rotations.rotatePointAroundZ(self.C, theta)
        
    def rotateAroundPointInX(self, p1, theta):
        """
        Rotates around a given point in X axis
        p1: point to rotate around
        theta: angle in rads to rotate by
        """
        self.A = rotations.rotatePointAroundPointInX(self.A, p1, theta)
        self.B = rotations.rotatePointAroundPointInX(self.B, p1, theta)
        self.C = rotations.rotatePointAroundPointInX(self.C, p1, theta)
        
    def rotateAroundPointInY(self, p1, theta):
        """
        Rotates around a given point in Y axis
        p1: point to rotate around
        theta: angle in rads to rotate by
        """
        self.A = rotations.rotatePointAroundPointInY(self.A, p1, theta)
        self.B = rotations.rotatePointAroundPointInY(self.B, p1, theta)
        self.C = rotations.rotatePointAroundPointInY(self.C, p1, theta)

    def rotateAroundPointInZ(self, p1, theta):
        """
        Rotates around a given point in Z axis
        p1: point to rotate around
        theta: angle in rads to rotate by
        """
        self.A = rotations.rotatePointAroundPointInZ(self.A, p1, theta)
        self.B = rotations.rotatePointAroundPointInZ(self.B, p1, theta)
        self.C = rotations.rotatePointAroundPointInZ(self.C, p1, theta)

    def translate(self, vector):
        """
        Moves the triangle
        vector: (x, y, z) tuple to move triangle by
        """
        self.A = c_mathhelp.addPoint(self.A, vector)
        self.B = c_mathhelp.addPoint(self.B, vector)
        self.C = c_mathhelp.addPoint(self.C, vector)
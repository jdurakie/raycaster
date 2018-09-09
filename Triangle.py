#TRIANGLES DEFINED COUNTER-CLOCK WISE:
#     C
#    / \
#   /   \
#  /     \
# A-------B

import mathhelp
import rotations

class Triangle(object):
    def __init__(self, A, B, C, color=(0,255,0), id=0):
        self.A = A
        self.B = B
        self.C = C
        self.color = color
        self.id = id

    def normal(self):
        p1 = mathhelp.subtractPoint(self.B, self.A)
        p2 = mathhelp.subtractPoint(self.C, self.A)
        return mathhelp.cross(p1, p2)
        
    def rotateAroundAxes(self, theta_x, theta_y, theta_z):
        if theta_x != 0:
            self.A = rotations.rotatePointAroundX(self.A, theta_x)
            self.B = rotations.rotatePointAroundX(self.B, theta_x)
            self.C = rotations.rotatePointAroundX(self.C, theta_x)
        #TODO : other rotation axes
        
    def rotateAroundPoint(self, p1, theta_x, theta_y, theta_z)
        pass

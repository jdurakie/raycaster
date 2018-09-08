#TRIANGLES DEFINED COUNTER-CLOCK WISE:
#     C
#    / \
#   /   \
#  /     \
# A-------B

import mathhelp

class Triangle(object):
    def __init__(self, A, B, C, color=(0,255,0)):
        self.A = A
        self.B = B
        self.C = C
        self.color = color

    def normal(self):
        p1 = mathhelp.subtractPoint(self.B, self.A)
        p2 = mathhelp.subtractPoint(self.C, self.A)
        return mathhelp.cross(p1, p2)
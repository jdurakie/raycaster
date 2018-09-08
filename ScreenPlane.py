
# AXIS ORIENTATIONS
# (Z into screen/away from view)
# Screen plane always has Z depth of 0
#    Z
#   /
#  /
# 0----------------------X (width)
# |             |     
# |    SCREEN   |
# |             |
# |-------------
# |
# Y (height)

import Line

class ScreenPlane(object):
    def __init__(self, width, height, focalDistance):
        self.width = width
        self.height = height
        self.focalDistance = focalDistance

        self.focalPointX = width/2.0
        self.focalPointY = height/2.0
        self.focalPointZ = -1 * focalDistance

        self.focalPoint = (self.focalPointX, self.focalPointY, self.focalPointZ)

    def rayGenerator(self):
        for x in range(0, self.width):
            for y in range(0, self.height):
                screenPoint = (x, y, 0)
                yield (Line.Line(self.focalPoint, screenPoint), (x, y))

    

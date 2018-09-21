"""
Used by mazewalker, generates maze segments to fly through
"""
# CUBE VERTEX NAMES
# (E-F-H-G square closer to view)
#    H-------G
#   /|      /|
#  / |     / |
# D-------C  |
# |  E----|--F
# | /     | /
# |/      |/
# A-------B


from Triangle import Triangle as T
import colormanip
from colormanip import GRAY

class Maze(object):
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.depth = max(self.screen_height, self.screen_width)
        self.A = (0, self.screen_height, 0)
        self.B = (self.screen_width, self.screen_height, 0)
        self.C = (self.screen_width, 0, 0)
        self.D = (0, 0, 0)
        self.E = (0, self.screen_height, self.depth)
        self.F = (self.screen_width, self.screen_height, self.depth)
        self.G = (self.screen_width, 0, self.depth)
        self.H = (0, 0, self.depth)

    #SEGMENT GENERATION
    def floor(self, color):
        return [
            T(self.A, self.B, self.F, color=colormanip.randomColorTimeBased()),
            T(self.F, self.E, self.A, color=colormanip.randomColorTimeBased())
        ]

    def leftWall(self, color):
        return [
            T(self.A, self.D, self.H, color=colormanip.randomColorTimeBased()),
            T(self.H, self.E, self.A, color=colormanip.randomColorTimeBased())
        ]

    def rightWall(self, color):
        return [
            T(self.B, self.F, self.G, color=colormanip.randomColorTimeBased()),
            T(self.G, self.C, self.B, color=colormanip.randomColorTimeBased()),
        ]

    def ceiling(self, color):
        return [
            T(self.C, self.G, self.H, color=colormanip.randomColorTimeBased()),
            T(self.H, self.D, self.C, color=colormanip.randomColorTimeBased())
        ]

    def backWall(self, color):
        return [
            T(self.F, self.E, self.H, color=colormanip.randomColorTimeBased()),
            T(self.H, self.G, self.F, color=colormanip.randomColorTimeBased())
        ]

    def corridor(self, floor_color=GRAY, wall_color=GRAY, ceil_color=GRAY):
        return self.floor(floor_color) + \
               self.leftWall(wall_color) + \
               self.rightWall(wall_color) + \
               self.ceiling(ceil_color)

    def rightTurn(self, floor_color=GRAY, wall_color=GRAY, ceil_color=GRAY):
        return self.floor(floor_color) + \
               self.leftWall(wall_color) + \
               self.backWall(wall_color) + \
               self.ceiling(ceil_color)

    def leftTurn(self, floor_color=GRAY, wall_color=GRAY, ceil_color=GRAY):
        return self.floor(floor_color) + \
               self.rightWall(wall_color) + \
               self.backWall(wall_color) + \
               self.ceiling(ceil_color)

    def upTurn(self, floor_color=GRAY, wall_color=GRAY, ceil_color=GRAY):
        return self.floor(floor_color) + \
               self.leftWall(wall_color) + \
               self.rightWall(wall_color) + \
               self.backWall(wall_color)

    def downTurn(self, floor_color=GRAY, wall_color=GRAY, ceil_color=GRAY):
        return self.leftWall(wall_color) + \
               self.rightWall(wall_color) + \
               self.backWall(wall_color) + \
               self.ceiling(ceil_color)

    def tJunctionLeft(self, floor_color=GRAY, wall_color=GRAY, ceil_color=GRAY):
        return self.rightWall(wall_color) + \
               self.floor(floor_color) + \
               self.ceiling(ceil_color)

    def tJunctionRight(self, floor_color=GRAY, wall_color=GRAY, ceil_color=GRAY):
        return self.leftWall(wall_color) + \
               self.floor(floor_color) + \
               self.ceiling(ceil_color)

    def tJunctionUp(self, floor_color=GRAY, wall_color=GRAY, ceil_color=GRAY):
        return self.floor(floor_color) + \
               self.leftWall(wall_color) + \
               self.rightWall(wall_color)

    def tJunctionDown(self, floor_color=GRAY, wall_color=GRAY, ceil_color=GRAY):
        return self.leftWall(wall_color) + \
               self.rightWall(wall_color) + \
               self.ceiling(wall_color)


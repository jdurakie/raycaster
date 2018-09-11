import ImageRenderer
import Sphere
import Triangle
import ScreenPlane
import mathhelp
import colormanip
import meshbuilder
import Maze
import rotations
import mazewalker

import cProfile
import re


# RENDERS SPHERE MOVING TOP-LEFT TO BOTTOM-RIGHT
# FOCAL_DISTANCE = 32
# SCREEN_WIDTH = 64
# SCREEN_HEIGHT = 32
#
# screen = ScreenPlane.ScreenPlane(SCREEN_WIDTH, SCREEN_HEIGHT, FOCAL_DISTANCE)
#
# for i in range(0, SCREEN_HEIGHT):
#     ir = ImageRenderer.ImageRenderer((SCREEN_WIDTH, SCREEN_HEIGHT))
#     sphere = Sphere.Sphere((i * 2, i, 16), 15)
#     rayGen = screen.rayGenerator()
#     while True:
#         try:
#             ray, screenCoord = next(rayGen)
#         except StopIteration:
#             break
#         if mathhelp.lineImpactsSphere(sphere, ray):
#             ir.point(screenCoord, color=(128, 128, 128))
#     ir.saveImage('outputs/output' + str(i) + '.png')

# RENDERS A TRIANGLE
# screen = ScreenPlane.ScreenPlane(64, 32, 32)
# ir = ImageRenderer.ImageRenderer((64, 32))
# triangle = Triangle.Triangle((3, 3, 20),
#                             (30, 3, 20),
#                             (15, 15, 15))
# rayGen = screen.rayGenerator()
# while True:
#     try:
#         ray, screenCoord = next(rayGen)
#     except StopIteration:
#         break
#     intersection = mathhelp.triangleLineIntersect(triangle, ray)
#     if intersection is not None:
#         shade = colormanip.getShade(triangle, ray, intersection)
#         R = int(128 * shade)
#         ir.point(screenCoord, color=(R, R, R))
#
# ir.saveImage('outputs/triangle.png')


def castRay(ray, tris):
    #find closest intersection
    nearestIntersectionZ = float('inf')
    nearestIntersectionColor = (0, 0, 0)
    for triangle in tris:
        intersection = mathhelp.triangleLineIntersect(triangle, ray)
        if intersection is not None and intersection[2] > 0.0 and intersection[2] < nearestIntersectionZ:
            nearestIntersectionZ = intersection[2]
            shade = colormanip.getShade(triangle, ray, intersection)
            R = int(triangle.color[0] * shade)
            G = int(triangle.color[1] * shade)
            B = int(triangle.color[2] * shade)
            nearestIntersectionColor = (R, G, B)
    return nearestIntersectionColor

def maze():
    corridor = Maze.Maze(32, 32).downTurn()
    screen = ScreenPlane.ScreenPlane(64, 32, 20)

    for tri in corridor:
        tri.translate((16, 0, 0))

    for i in range(0, 30):    
        ir = ImageRenderer.ImageRenderer((64, 32))
        rayGen = screen.rayGenerator()
        rotations.rotateTrisAroundCentroidInX(corridor, 0.1)
        while True:
            try:
                ray, screenCoord = next(rayGen)
            except StopIteration:
                break
            ir.point(screenCoord, castRay(ray, corridor))

        ir.saveImage('outputs/maze' + str(i) + '.png')

def drawBox():
    screen = ScreenPlane.ScreenPlane(64, 32, 20)
    tris = meshbuilder.makeBox()
    for i in range(0, 300, 5):
        ir = ImageRenderer.ImageRenderer((64, 32))
        rayGen = screen.rayGenerator()
        while True:
            try:
                ray, screenCoord = next(rayGen)
            except StopIteration:
                break
            ir.point(screenCoord, castRay(ray, tris))
        for tri in tris:
            #tri.rotateAroundPoint((15, 15, 30), -0.1, 0, 0)
            tri.rotateAroundPointInX((32, 16, 30), -0.1)
            tri.rotateAroundPointInY((32, 16, 30), -0.2)
            tri.rotateAroundPointInZ((32, 16, 30), -0.3)
            #tri.translate((1, 0, -1))
        print('Done with step ' + str(i))
        ir.saveImage('outputs/triangle' + str(i) + '.png')
#drawBox()
#maze()

mazewalker.mazewalker(64, 32)

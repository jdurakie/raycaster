import ImageRenderer
import Sphere
import Triangle
import ScreenPlane
import mathhelp
import colormanip
import meshbuilder


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

screen = ScreenPlane.ScreenPlane(64, 32, 32)
ir = ImageRenderer.ImageRenderer((64, 32))

tris = meshbuilder.pointsToTriangles([])
rayGen = screen.rayGenerator()

while True:
    try:
        ray, screenCoord = next(rayGen)
    except StopIteration:
        break
    for triangle in tris:
        intersection = mathhelp.triangleLineIntersect(triangle, ray)
        if intersection is not None:
            shade = colormanip.getShade(triangle, ray, intersection)
            R = int(255 * shade)
            ir.point(screenCoord, color=(R, R, R))

ir.saveImage('outputs/triangleboth.png')

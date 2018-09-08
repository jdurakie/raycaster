import ImageRenderer
import Sphere
import ScreenPlane
import mathhelp

FOCAL_DISTANCE = 32
SCREEN_WIDTH = 64
SCREEN_HEIGHT = 32

screen = ScreenPlane.ScreenPlane(SCREEN_WIDTH, SCREEN_HEIGHT, FOCAL_DISTANCE)

for i in range(0, SCREEN_HEIGHT):
    ir = ImageRenderer.ImageRenderer((SCREEN_WIDTH, SCREEN_HEIGHT))
    sphere = Sphere.Sphere((i * 2, i, 16), 15)
    rayGen = screen.rayGenerator()
    while True:
        try:
            ray, screenCoord = next(rayGen)
        except StopIteration:
            break
        if mathhelp.lineImpactsSphere(sphere, ray):
            ir.point(screenCoord, color=(128, 128, 128))
    ir.saveImage('outputs/output' + str(i) + '.png')

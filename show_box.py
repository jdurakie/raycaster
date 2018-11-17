import ScreenPlane
import meshbuilder
import rotations
#import PngImageRenderer as ImageRenderer
import CursesImageRenderer as ImageRenderer
import c_mathhelp
import time
import math

def show_box(width, height):
	
	#set up screen
	screen = ScreenPlane.ScreenPlane(width, height, 70)
	#create output image
	image = ImageRenderer.ImageRenderer((width, height))
	#create box mesh
	boxMesh = meshbuilder.makeBox()
	#rotate the box around a little
	while(True):
		rotations.rotateTrisAroundCentroidInX(boxMesh, math.sin(time.time()) / 10)
		rotations.rotateTrisAroundCentroidInY(boxMesh, math.sin(time.time()) / 10)
		rotations.rotateTrisAroundCentroidInZ(boxMesh, 0.1)
		#start casting some rays and drawing them on output image
		rayGenerator = screen.rayGenerator()
		while True:
			try:
				ray, screenCoord = next(rayGenerator)
			except StopIteration:
				break
			image.point(screenCoord, c_mathhelp.castRay(ray, boxMesh, len(boxMesh)))
		image.saveImage('outputs/box.png')

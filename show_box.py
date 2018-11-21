import ScreenPlane
import meshbuilder
import rotations
#import PngImageRenderer as ImageRenderer
#import CursesImageRenderer as ImageRenderer #BROKEN WHILE BENCHMARKING CODE IS INCLUDED
import PygameRenderer as ImageRenderer
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
	#rotate the box around a little while keeping track of FPS
	lastFrameTime = time.time()
	frameCount = 0
	totalFrameTime = 0
	while(True):
		rotations.rotateTrisAroundCentroidInX(boxMesh, math.sin(time.time()) / 10)
		rotations.rotateTrisAroundCentroidInY(boxMesh, math.sin(time.time()) / 10)
		rotations.rotateTrisAroundCentroidInZ(boxMesh, 0.1)
		#start casting some rays and drawing them on output image
		rayGenerator = screen.rayGenerator()

		# Genreate one ray and cast it immediately before moving on to the next ray
		# Generating all rays at once is actually slower
		while True:
			try:
				ray, screenCoord = next(rayGenerator)
			except StopIteration:
				break
			image.point(screenCoord, c_mathhelp.castRay(ray, boxMesh, len(boxMesh)))

		image.saveImage('outputs/box.png')

		#Some benchmarking display code
		sinceLastFrame = time.time() - lastFrameTime
		lastFrameTime = time.time()
		totalFrameTime += sinceLastFrame
		frameCount += 1
		if frameCount == 10:
			avgFrameTime = totalFrameTime / 10
			fps = 1 / avgFrameTime
			print("AVG FPS: " + str(fps))
			frameCount = 0
			totalFrameTime = 0
`
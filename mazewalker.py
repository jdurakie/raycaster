"""
Rendering engine demo, creates a maze that the viewpoint flies through
"""
import Maze
import random
import c_mathhelp as mathhelp
import colormanip
import PngImageRenderer as ImageRenderer
import ScreenPlane
import rotations

def castRay(ray, tris):
    #find closest intersection
    nearestIntersectionZ = float('inf')
    nearestIntersectionColor = (0, 0, 0)
    for triangle in tris:
        intersection = mathhelp.triangleLineIntersect(triangle.A, triangle.B, triangle.C, 
                                                      ray.start, ray.end)
        if intersection is not None and intersection[2] > 0.0 and intersection[2] < nearestIntersectionZ:
            nearestIntersectionZ = intersection[2]
            shade = colormanip.getShade(triangle, ray, intersection)
            R = int(triangle.color[0] * shade)
            G = int(triangle.color[1] * shade)
            B = int(triangle.color[2] * shade)
            nearestIntersectionColor = (R, G, B)
    return nearestIntersectionColor

def translate(tris, vector):
    for tri in tris:
        tri.translate(vector)

def mazewalker(width, height, mazeLength=10):
    #maze segments should be cubes
    depth = min(width, height)
    M = Maze.Maze(depth, depth)

    choices = ['straight', 'up', 'down', 'left', 'right']
    lastLocation = (16, 0, 0)

    startingCorridor = M.corridor()
    elements = [startingCorridor]
    elementTypes = ['straight']
    translate(startingCorridor, (16, 0, 0))
    lastLocation = mathhelp.addPoint(lastLocation, (0, 0, depth))


    screen = ScreenPlane.ScreenPlane(width, height, 20)
    i = 0
    while True:
        i += 1
        #generate next maze element:
        if len(elements) < 5:
            nextElement = random.choice(choices)
            if nextElement == 'straight':
                elem = M.corridor()
                translate(elem, lastLocation)
                elements.append(elem)
                elementTypes.append('straight')
                lastLocation = mathhelp.addPoint(lastLocation, (0, 0, depth))

            if nextElement == 'right':
                #generate right turn                
                elem = M.rightTurn() 
                translate(elem, lastLocation)
                lastLocation = mathhelp.addPoint(lastLocation, (depth, 0, 0))
                #generate t-junction to end right turn
                nextElem = M.tJunctionLeft()
                translate(nextElem, lastLocation)
                lastLocation = mathhelp.addPoint(lastLocation, (0, 0, depth))
                finalElem = elem + nextElem
                #need to translate turn + junction to last location
                elements.append(finalElem)
                elementTypes.append('right')
            if nextElement == 'left':
                #generate left turn                
                elem = M.leftTurn() 
                translate(elem, lastLocation)
                lastLocation = mathhelp.addPoint(lastLocation, (-1 * depth, 0, 0))
                #generate t-junction to end left turn
                nextElem = M.tJunctionRight()
                translate(nextElem, lastLocation)
                lastLocation = mathhelp.addPoint(lastLocation, (0, 0, depth))
                finalElem = elem + nextElem
                #need to translate turn + junction to last location
                elements.append(finalElem)
                elementTypes.append('left')
            if nextElement == 'down':
                #generate down turn                
                elem = M.downTurn() 
                translate(elem, lastLocation)
                lastLocation = mathhelp.addPoint(lastLocation, (0, depth, 0))
                #generate t-junction to end down turn
                nextElem = M.tJunctionUp()
                translate(nextElem, lastLocation)
                lastLocation = mathhelp.addPoint(lastLocation, (0, 0, depth))
                finalElem = elem + nextElem
                #need to translate turn + junction to last location
                elements.append(finalElem)
                elementTypes.append('down')
            if nextElement == 'up':
                #generate up turn
                elem = M.upTurn()
                translate(elem, lastLocation)
                lastLocation = mathhelp.addPoint(lastLocation, (0, -depth, 0))
                #generate t-junction to end up turn
                nextElem = M.tJunctionDown()
                translate(nextElem, lastLocation)
                lastLocation = mathhelp.addPoint(lastLocation, (0, 0, depth))
                finalElem = elem + nextElem
                #need to translate turn + junction to last location
                elements.append(finalElem)
                elementTypes.append('up')


        if len(elements) > 3:
            tris = []
            for element in elements:
                tris = tris + element
            for j in range(0, depth):
                ir = ImageRenderer.ImageRenderer((width, height))
                rayGen = screen.rayGenerator()
                while True:
                    try:
                        ray, screenCoord = next(rayGen)
                        if screenCoord[0] < 17 or screenCoord[0] >= 47:
                            continue
                    except StopIteration:
                        break
                    #ir.point(screenCoord, castRay(ray, tris))
                    ir.point(screenCoord, mathhelp.castRay(ray, tris, len(tris)))
                ir.saveImage('outputs/mazewalker' + str(i) + '-' + str(j) + '.png')
                #move 'camera' based on segment
                if elementTypes[0] == 'straight':
                    translate(tris, (0, 0, -1))
                elif elementTypes[0] == 'right':
                    translate(tris, (-1, 0, -1))
                elif elementTypes[0] == 'left':
                    translate(tris, (1, 0, -1))
                elif elementTypes[0] == 'down':
                    translate(tris, (0, -1, -1))
                elif elementTypes[0] == 'up':
                    translate(tris, (0, 1, -1))
            #move location of next element based on where we went
            if elementTypes[0] == 'straight':
                lastLocation = mathhelp.addPoint(lastLocation, (0, 0, -depth))
            elif elementTypes[0] == 'right':
                lastLocation = mathhelp.addPoint(lastLocation, (-depth, 0, -depth))
            elif elementTypes[0] == 'left':
                lastLocation = mathhelp.addPoint(lastLocation, (depth, 0, -depth))
            elif elementTypes[0] == 'down':
                lastLocation = mathhelp.addPoint(lastLocation, (0, -depth, -depth))
            elif elementTypes[0] == 'up':
                lastLocation = mathhelp.addPoint(lastLocation, (0, depth, -depth))
            print("walked " + elementTypes[0])
            elementTypes.pop(0)
            elements.pop(0)
            



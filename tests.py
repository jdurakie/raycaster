"""
Random little tests.
"""

import mathhelp
import c_mathhelp
import Line
import Triangle
import rotations
import math

print('---------------mathhelp')
print('\tmagnitude')
p1 = (4, 0, 7)
print (c_mathhelp.magnitude(p1))
print ('expected about 8')

p2 = (-2, 1, 3)
print('\tangleBetweenLines')
print(mathhelp.angleBetweenLines(p1, p2))

print('\tdistanceFromPointToLine')
l = Line.Line((0, 0, 0), (3, 0, 0))
print(mathhelp.distanceFromPointToLine((-10, -1, -1), l))


print('\tdistanceFromPointToLine2')
l = Line.Line((0, 0, 0), (3, 0, 0))
print(mathhelp.distanceFromPointToLine2((-10, -1, -1), l))


print('\tdistanceFromPointToLine2')
l = Line.Line((0, 0, 0), (3, 0, 0))
print(mathhelp.distanceFromPointToLine2((0, 3, 0), l))


# print('\ttriangleLineIntesect')
# l = Line.Line((0, 0, 0), (1, 0, 6))
# t = Triangle.Triangle((-1, -1, 3), (1, -1, 3), (0, 1, 3))
# print(c_mathhelp.triangleLineIntersect(t, l))

print('---------------Line')
print('\tnormalize')
l = Line.Line((1, 1, 1), (2, 2, 2))
print (l.vectorize())

print('---------------ColorManip')
print('\tgetShade')
print("TODO")

print('---------------Rotations')
print('\tapplyRotationMatrix')
p = (1, 2, 3)
R = [[1, 2, 3],
     [4, 5, 6],
	 [7, 8, 9]]
print(rotations.applyRotationMatrix(p, R))

print('----------------Triangles')
print('\tboundingRadius')
t = Triangle.Triangle((0, 0, 0), (10, 0, 0), (5, 10, 0))
print(t.boundingRadius())
print('\tcentroid')
print(t.centroid())

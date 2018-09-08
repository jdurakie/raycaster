import mathhelp
import Line
import Triangle

print('---------------mathhelp')
print('\tmagnitude')
p1 = (4, 0, 7)
print (mathhelp.magnitude(p1))
print ('expected about 8')

p2 = (-2, 1, 3)
print('\tangleBetweenLines')
print(mathhelp.angleBetweenLines(p1, p2))

print('\tdistanceFromPointToLine')
l = Line.Line((0, 0, 0), (3, 0, 0))
print(mathhelp.distanceFromPointToLine((-10, -1, -1), l))

print('\ttriangleLineIntesect')
l = Line.Line((0, 0, 0), (0, 0, 10))
t = Triangle.Triangle((-1, -1, 5), (1, -1, 5), (0, 1, 5))
print(mathhelp.triangleLineIntersect(t, l))

print('---------------Line')
print('\tnormalize')
l = Line.Line((1, 1, 1), (2, 2, 2))
print (l.normalize())





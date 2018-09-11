import Line
import Triangle
import mathhelp
print('\ttriangleLineIntesect')
for i in range(0, 100000):
    l = Line.Line((0, 0, 0), (1, 0, 6))
    t = Triangle.Triangle((-1, -1, 3), (1, -1, 3), (0, 1, 3))
    mathhelp.triangleLineIntersect(t, l)
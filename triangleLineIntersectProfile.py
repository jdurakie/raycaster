"""
Test file meant to profile/benchmark the crucial TriangleLineIntersect function
"""
import Line
import Triangle
import c_mathhelp
print('\ttriangleLineIntesect')
l = Line.Line((0, 0, 0), (1, 0, 6))
t = Triangle.Triangle((-1, -1, 3), (1, -1, 3), (0, 1, 3))
for i in range(0, 100000):
    c_mathhelp.triangleLineIntersect(t.A, t.B, t.C, l.start, l.end)
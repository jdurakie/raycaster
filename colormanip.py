import Line
import mathhelp

def getShade(triangle, ray, intersection):
    ray = mathhelp.normalize(Line.Line(ray.start, intersection).vectorize())
    trinorm = mathhelp.normalize(triangle.normal())
    dot = mathhelp.dotproduct(ray, trinorm)
    return (0.3 + (0.7 * abs(dot)))

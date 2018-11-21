from Triangle import Triangle as T
from colormanip import RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA
def makeBox():
    A = (22, 26, 20)
    B = (42, 26, 20)
    C = (42,  6, 20)
    D = (22,  6, 20)
    E = (22, 26, 40)
    F = (42, 26, 40)
    G = (42,  6, 40)
    H = (22,  6, 40)
    tris = [
        T(A, B, C, color=RED),
        T(C, D, A, color=RED),
        T(B, F, C, color=GREEN),
        T(F, G, C, color=GREEN),
        T(D, C, G, color=BLUE),
        T(G, H, D, color=BLUE),
        T(E, A, D, color=YELLOW),
        T(D, H, E, color=YELLOW),
        T(A, E, F, color=CYAN),
        T(F, B, A, color=CYAN),
        T(E, H, G, color=MAGENTA),
        T(G, F, E, color=MAGENTA)
    ]
    return tris

def makeTriangle():
    A = (30, 30, 30)
    B = (60, 30, 30)
    C = (45, 55.981, 30)


    return [T(A, B, C, color=RED)]


def makeBox2(center, diameter):
    # CUBE VERTEX NAMES
    #    H-------G
    #   /|      /|
    #  / |     / |
    # D-------C  |
    # |  E----|--F
    # | /     | /
    # |/      |/
    # A-------B

    cX = center[0]
    cY = center[1]
    cZ = center[2]

    minX = cX - diameter
    minY = cY - diameter
    minZ = cZ - diameter

    maxX = cX + diameter
    maxY = cY + diameter
    maxZ = cZ + diameter

    A = (minX, minY, minZ)
    B = (maxX, minY, minZ)
    C = (maxX, maxY, minZ)
    D = (minX, maxY, minZ)
    E = (minX, minY, maxZ)
    F = (maxX, minY, maxZ)
    G = (maxX, maxY, maxZ)
    H = (minX, maxY, maxZ)

    tris = [
        T(A, B, C, color=RED),
        T(C, D, A, color=RED),
        T(B, F, C, color=GREEN),
        T(F, G, C, color=GREEN),
        T(D, C, G, color=BLUE),
        T(G, H, D, color=BLUE),
        T(E, A, D, color=YELLOW),
        T(D, H, E, color=YELLOW),
        T(A, E, F, color=CYAN),
        T(F, B, A, color=CYAN),
        T(E, H, G, color=MAGENTA),
        T(G, F, E, color=MAGENTA)
    ]
    return tris

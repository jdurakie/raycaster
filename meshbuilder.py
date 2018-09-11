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
from Triangle import Triangle as T
def pointsToTriangles(points):
    #
    #for i in range(0, len(points - 2)):

    # A = (3, 3, 20)
    # B = (30, 3, 20)
    # C = (3, 30, 20)
    # D = (30, 30, 40)
    # tris = [
    # T(B, D, C, id=0),
    # T(A, B, C, id=1)
    # ]

    # A = (3, 3, 20)
    # B = (3, 30, 20)
    # D = (30, 30, 20)
    # E = (3, 2, 40)
    # tris = [
    # T(B, B, D, id=0),
    # T(A, D, E, id=1)
    # ]

    A = (3, 30, 20)
    B = (30, 30, 20)
    C = (30, 3, 20)
    D = (3, 3, 20)
    E = (6, 28, 40)
    F = (38, 14, 40)
    G = (38, -13, 40)
    H = (6, -13, 40)
    tris = [
    T(A, B, C),
    T(C, D, A),
    T(D, C, H),
    T(C, G, H),
    T(B, F, C),
    T(F, G, C)
    ]
    return tris

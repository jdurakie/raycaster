import linalg

print("Testing CROSS:")
print("\t" + str(linalg.cross((1, 0, 0), (0, 1, 1))))
print("\t" + str(linalg.cross((10, 0, 0), (5, 10, 0))))

print("Testing SUBTRACT POINT:")
print("\t" + str(linalg.subtractPoint((1, 2, 3.3), (0.1, 1, 3.1))))

print("Testing ADD POINT:")
print("\t" + str(linalg.addPoint((1, 2, 3.3), (0.1, 1, 3.1))))

print("Testing MAGNITUDE:")
print("\t" + str(linalg.magnitude((1, 1, 1))))

print("Testing NORMALIZE:")
print("\t" + str(linalg.normalize((10, 10, 10))))

print("Testing DOT PRODUCT:")
print("\t" + str(linalg.dotProduct((10, 10, 10), (10, 15, 5))))

print("Testing MULTIPLY BY SCALAR:")
print("\t" + str(linalg.multiplyByScalar((1, 2, 3), 3)))

print("Testing TRIANGLE LINE INTERSECT:")
tA = (0, 0, 0)
tB = (10, 0, 0)
tC = (5, 10, 0)
start = (5, 2, -1)
end = (5, 2, 1)
intersection = linalg.triangleLineIntersect(tA, tB, tC, start, end)
print("\t" + str(intersection))

# start = (5, 2, -1)
# end = (5, 3, -1.01)
# intersection = linalg.triangleLineIntersect(tA, tB, tC, start, end)
# print("\t" + str(intersection))

# start = (100, 100, 100)
# end = (100, 100, 101)
# intersection = linalg.triangleLineIntersect(tA, tB, tC, start, end)
# print("\t" + str(intersection))

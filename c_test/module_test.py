import linalg

print("Testing CROSS:")
print("\t" + str(linalg.cross((1, 0, 0), (0, 1, 1))))



print("Testing SUBTRACT POINT:")
print("\t" + str(linalg.subtractPoint((1, 2, 3.3), (0.1, 1, 3.1))))


print("Testing MAGNITUDE:")
print("\t" + str(linalg.magnitude((1, 1, 1))))


print("Testing NORMALIZE:")
print("\t" + str(linalg.normalize((10, 10, 10))))
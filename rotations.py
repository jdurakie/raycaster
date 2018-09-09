import math
from math import sin, cos
import mathhelp

def applyRotationMatrix(p1, R):
	R_lft = [R[0][0], R[1][0], R[2][0]]
	R_mid = [R[0][1], R[1][1], R[2][1]]
	R_bot = [R[0][2], R[1][2], R[2][2]]
	x = sum([p1[0] * R[0][0], p1[1] * R[1][0], p1[2] * R[2][0]])
	y = sum([p1[0] * R[0][1], p1[1] * R[1][1], p1[2] * R[2][1]])
	z = sum([p1[0] * R[0][2], p1[1] * R[1][2], p1[2] * R[2][2]])
	return (x, y, z)
	
def rotatePointAroundX(p1, theta):
	Rx = [[1, 		   0, 			  0],
	      [0, cos(theta), -1*sin(theta)],
		  [0, sin(theta),    cos(theta)]]
	
	return applyRotationMatrix(p1, Rx)


def rotatePointAroundPoint(p1, p2, theta_x, theta_y, theta_z):
    translatedPoint = mathhelp.subtractPoint(p1, p2)
    if theta_x != 0:
        translatedPoint = rotatePointAroundX(translatedPoint, theta_x)
        
    #un-translate the point
    return mathhelp.addPoint(translatedPoint, p2)
		  
		  
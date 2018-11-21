import c_mathhelp

class ShapeMesh(object):
	def __init__(self, tris):
		self.tris = tris
		self.tris_len = len(tris)
		self.mesh_centroid = None
		self.bounding_sphere_radius = None
		self._calculateCentroid()

	# def _calculateBoundingSphere(self):
	# 	if self.mesh_centroid == None:
	# 		self._calculateCentroid()
	# 	farthest_vtx_mag = 0
	# 	for tri in self.tris:
	# 		for vtx in [tri.A, tri.B, tri.C]:
	# 			vtx_dist = c_mathhelp.subtractPoint(vtx, self.mesh_centroid)
	# 			vtx_mag = c_mathhelp.magnitude(vtx_dist)
	# 			if farthest_vtx_mag < vtx_mag:
	# 				farthest_vtx_mag = vtx_mag
	# 	self.bounding_sphere_radius = farthest_vtx_mag

	def _calculateCentroid(self):
		mesh_centroid = (0, 0, 0)
		for tri in self.tris:
			tri_centroid = tri.centroid()
			mesh_centroid = c_mathhelp.addPoint(mesh_centroid, tri_centroid)

		self.mesh_centroid = c_mathhelp.multiplyPointByScalar(mesh_centroid, 1.0 / len(self.tris))

	def rotateAroundCentroidInX(self, theta):
		for tri in self.tris:
			tri.rotateAroundPointInX(self.mesh_centroid, theta)

	def rotateAroundCentroidInY(self, theta):
		for tri in self.tris:
			tri.rotateAroundPointInY(self.mesh_centroid, theta)

	def rotateAroundCentroidInZ(self, theta):
		for tri in self.tris:
			tri.rotateAroundPointInZ(self.mesh_centroid, theta)


graph = {
	'u' : ['u', 'x'],
	'x' : ['v'],
	'v' : ['y'],
	'y' : ['x'],
	'w' : ['y', 'z'],
	'z' : ['z'],
}

W = "white"
G = "gray"
B = "black"

class DFS():
	def __init__(self, g):
		self._g = g
		self._color = dict()
		self._time = 0
		for k in self._g.iterkeys():
			self._color[k] = W

	def DFS_Visit(self, vertex):
		self._color[vertex] = G
		self._time += 1
		#print vertex, self._time
		for v in self._g[vertex]:
			if self._color[v] == W:
				self.DFS_Visit(v)
		self._color[vertex] = B
		self._time += 1
		#print vertex, self._time

	def Traverse(self):
		for vertex in self._g.iterkeys():
			if self._color[vertex] == W:
				self.DFS_Visit(vertex)

DFS(graph).Traverse()

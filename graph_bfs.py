
graph1 = {'A': ['B', 'C'],
	'B': ['C', 'D'],
	'C': ['D'],
	'D': ['C'],
	'E': ['F'],
	'F': ['C']}

graph2 = {
	's' : ['r', 'w'],
	'r' : ['v'],
	'v'	: ['r'],
	'w' : ['s', 't', 'x'],
	't' : ['w', 'x', 'u'],
	'x' : ['w', 't', 'u', 'y'],
	'u' : ['t', 'x', 'y'],
	'y' : ['u', 'x'],
}

W = "white"
G = "gray"
B = "black"

def BFS(g, start):
	color = dict()
	q = list()
	for k in g.iterkeys():
		color[k] = W

	color[start] = G
	q.append(start)
	while len(q) > 0:
		node = q.pop(0)
		for child in g[node]:
			if color[child] == W:
				color[child] = G
				q.append(child)
		color[node] = B
		print node

class Graph():
	def __init__(self, g):
		self._color = dict()
		self._g = g
		self.Clear()

	def Clear(self):
		for k in self._g.iterkeys():
			self._color[k] = W

	def BFS(self, start):
		if self._color[start] == W:
			self._color[start] = G
		else:
			return

		self._color[start] = B
		print start
		for child in self._g[start]:
			self.BFS(child)

#BFS(graph, 'A')
BFS(graph2, 's')
print "-----"
g = Graph(graph2)
g.BFS('s')

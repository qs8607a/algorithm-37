
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

#BFS(graph, 'A')
BFS(graph2, 's')

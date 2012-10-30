class BinaryTree():
	def __init__(self):
		self._root = None

	def Search(self, node):
		return self._Search(self._root, node)

	def _Search(self, base, node):
		if base is None or node.v == base.v:
			return base

		if node.v > base.v:
			return self._Search(base.r, node)
		else:
			return self._Search(base.l, node)


	def Minimum(self):
		return self._Minimum(self._root)

	def _Minimum(self, p):
		while p.l is not None:
			p = p.l

		return p

	def Maximum(self):
		return self._Maximum(self._root)

	def _Maximum(self, p):
		while p.r is not None:
			p = p.r

		return p

	#INORDER
	def Predecessor(self, node):
		p = self.Search(node)
		if p.l is not None:
			return self._Maximum(p)

		y = p.p
		while y is not None and y.l == p:
			p = y
			y = y.p

		return y


	#INORDER
	def Successor(self, node):
		p = self.Search(node)
		if p.r is not None:
			return self._Minimum(p)

		y = p.p
		while y is not None and y.r == p:
			p = y
			y = y.p

		return y

	def Insert(self, node):
		if self._root is None:
			self._root = node
			return

		cur = self._root

		while cur is not None:
			p = cur
			if node.v > cur.v:
				cur = cur.r
				if cur is None:
					p.r = node
					node.p = p
					return
			else:
				cur = cur.l
				if cur is None:
					p.l = node
					node.p = p
					return

	def Delete(self, node):
		pass

	def InorderWalk(self):
		self.Walk(self._root)

	def Walk(self, p):
		if p is not None:
			self.Walk(p.l)
			l = None
			r = None
			if p.l is not None:
				l = p.l.v
			if p.r is not None:
				r = p.r.v
			print p.v, l, r
			self.Walk(p.r)

class Node():
	def __init__(self, v):
		self.v = v
		self.l = None
		self.r = None
		self.p = None

import random
t = BinaryTree()
max_ = 0
min_ = 1000
for i in xrange(10):
	num = random.randint(1,100)
	if num > max_:
		max_ = num
	if num < min_:
		min_ = num
	t.Insert(Node(num))

t.InorderWalk()
assert(t.Search(Node(num)) is not None)
assert(t.Search(Node(-1)) is None)
assert(t.Minimum().v == min_)
assert(t.Maximum().v == max_)

print num, t.Successor(Node(num)).v
print num, t.Predecessor(Node(num)).v


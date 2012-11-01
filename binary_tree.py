class BinaryTree():
	def __init__(self):
		self._root = None
		self._level = 0
		self._deep_lvl = 0
		self._deep_parent = 0

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
		self.RecursiveWalk(self._root)

	def Walk(self):
		stack = list()
		#stack.insert(0, self._root)

		top = self._root
		while top is not None or len(stack) > 0:
			if top is not None:
				stack.insert(0, top)
				top = top.l
				continue

			top = stack.pop(0)
			print "111", top

			top = top.r

	def RecursiveWalk(self, p):
		if p is not None:
			self._level += 1
			self.RecursiveWalk(p.l)
			l = None
			r = None
			if p.l is not None:
				l = p.l.v
			if p.r is not None:
				r = p.r.v
			if p.l is not None and \
				p.r is not None and \
				self._level > self._deep_lvl:
				self._deep_lvl = self._level
				self._deep_parent = p

			print self._level, p.v, l, r

			self.RecursiveWalk(p.r)
			self._level -= 1

class Node():
	def __init__(self, v):
		self.v = v
		self.l = None
		self.r = None
		self.p = None
	def __str__(self):
		return "%s" % self.v

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
t.Walk()
print t._deep_lvl, t._deep_parent.v

assert(t.Search(Node(num)) is not None)
assert(t.Search(Node(-1)) is None)
assert(t.Minimum().v == min_)
assert(t.Maximum().v == max_)
b = BinaryTree()
b.Insert(Node(2))
b.Insert(Node(1))
b.Insert(Node(3))
b.InorderWalk()
b.Walk()

print num, t.Successor(Node(num)).v
print num, t.Predecessor(Node(num)).v


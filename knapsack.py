class Item():
	def __init__(self, n, w, v):
		self.name = n
		self.weight = w
		self.value = v

	def __str__(self):
		return "%s:w=%d:s=%d" % ( self.name, self.weight, self.value)

## f(i,w) = {
## 	0 , 	(i == 0,)
## 	f(i - 1, w),  (i > 0, w - Wi < 0)
## 	max( f(i -1, w), f(i-1, w - Wi) + Vi), (i > 0, w - Wi >= 0)
## }
class Knapsack():
	def __init__(self):
		self._all_items = list()
		self._f = dict()
		self._count = 0

	def Add(self, item):
		self._f[len(self._all_items)] = dict()
		self._all_items.append(item)

	def Solve(self, size):
		print self.helper(len(self._all_items) - 1,  size)
		print self._count
		print self._f


	def GetWeight(self, i):
		if i < 0:
			return 0
		return self._all_items[i].weight

	def helper(self, i, w):
		try: return self._f[i][w]
		except KeyError:
			ret = 0
			if i < 0:
				return 0
			elif w - self.GetWeight(i) < 0:
				ret = self.helper(i - 1, w)
			else:
				ret = max(self.helper(i - 1, w),
					self.helper(i - 1, w - self.GetWeight(i)) + self._all_items[i].value)
			self._f[i][w] = ret
			self._count += 1
			return ret

k = Knapsack()
k.Add(Item("lz", 4, 4500))
k.Add(Item("pg", 5, 5700))
k.Add(Item("jz", 2, 2250))
k.Add(Item("cm", 1, 1100))
k.Add(Item("tg", 6, 6700))

k.Solve(8)


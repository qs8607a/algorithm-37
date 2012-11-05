import math
class Heap():
	def __init__(self, array):
		self._heap = array
		self._sorted = list()

	def ParentIndex(self, i):
		return int(math.ceil(i / 2.0 - 1))

	def Parent(self, i):
		return self._heap[self.ParentIndex(max(i, 0))]

	def LeftIndex(self, i):
		return 2 * i + 1

	def Left(self, i):
		return self._heap[self.LeftIndex(i)]

	def RightIndex(self, i):
		return 2 * (i + 1)

	def Right(self, i):
		return self._heap[self.RightIndex(i)]

	#obsoleted
	'''
	def Heapify(self, i = 0):
		if i >= len(self._heap):
			return

		l = self.LeftIndex(i)
		r = self.RightIndex(i)

		self.Heapify(l)
		self.Heapify(r)

		#print "index=%d, v=%d, p=%d" %(i, self._heap[i], self.Parent(i))
		if self._heap[i] > self.Parent(i):
			tmp =self._heap[i]
			self._heap[i] = self.Parent(i)
			self._heap[self.ParentIndex(i)] = tmp

			## after swap, heap order may be wrong, so heapify this node again.
			self.Heapify(i)
	'''

	def BuildHeap(self):
		i = (len(self._heap) - 1) / 2

		while i >= 0:
			self.MaxHeapify(i)
			i -= 1

	def _Swap(self, i, j):
		tmp =self._heap[i]
		self._heap[i] = self._heap[j]
		self._heap[j] = tmp


	def MaxHeapify(self, i = 0):
		l = self.LeftIndex(i)
		r = self.RightIndex(i)

		if l < len(self._heap) and self._heap[l] > self._heap[i]:
			largest = l
		else:
			largest = i

		if r < len(self._heap) and self._heap[r] > self._heap[largest]:
			largest = r

		if largest != i:
			self._Swap(i, largest)
			self.MaxHeapify(largest)

	def Insert(self, v):
		self._heap.append(v)
		#self.Heapify()
		self.IncreaseKey(len(self._heap) - 1, v)

	def Maximum(self):
		return self._heap[0]

	def ExtractMax(self):
		if len(self._heap) <= 0:
			return

		ret = self._heap[0]

		self._heap[0] = self._heap[len(self._heap) - 1]
		self._heap.pop()
		self.MaxHeapify(0)
		return ret

	def IncreaseKey(self, i, key):
		assert(key >= self._heap[i])
		self._heap[i] = key
		while i > 0 and self.Parent(i) < self._heap[i]:
			self._Swap(i, self.ParentIndex(i))
			i = self.ParentIndex(i)

	def Sort(self):
		ret = list()
		while len(self._heap) > 0:
			ret.append(self.ExtractMax())
		return ret


def main():
	a = [1,2,3,4,5,6]
	heap = Heap(a)
	heap.BuildHeap()
	print heap._heap
	heap.ExtractMax()
	print heap._heap
	heap.Insert(10)
	heap.Insert(7)
	print heap._heap
	print heap.Sort()

main()

import math
class Heap():
	def __init__(self, array):
		self._heap = array

	def ParentIndex(self, i):
		return int(math.ceil(i / 2.0 - 1))

	def Parent(self, i):
		if self.ParentIndex(i) < 0:
			return 100000000 ## a 'biggest' value

		return self._heap[self.ParentIndex(i)]

	def LeftIndex(self, i):
		return 2 * i + 1

	def Left(self, i):
		return self._heap[self.LeftIndex(i)]

	def RightIndex(self, i):
		return 2 * (i + 1)

	def Right(self, i):
		return self._heap[self.RightIndex(i)]

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



def main():
	a = [1,2,3,4,5,6]
	heap = Heap(a)
	heap.Heapify()
	print heap._heap


main()

a = [ 31, -41, 59, 26, -53, 58, 97, -93, -23, 84]

f = dict()

def sum(i, j):
	if i not in f:
		f[i] = dict()

	if j not in f[i]:
		if i != j:
			f[i][j] = sum(i, j - 1) + a[j]
		else:
			f[i][j] = a[j]

	return f[i][j]


def find_max():
	max_ = 0
	for i in xrange(0, len(a)):
		for j in xrange(i, len(a)):
			sum_ = sum(i, j)
			max_ = max(sum_, max_)
	print max_

def find_max():
	max_ = 0
	for i in xrange(0, len(a)):
		for j in xrange(i, len(a)):
			#sum_ = sum(i, j)
			sum_ = 0
			for k in xrange(i, j):
				sum_ += a[k]
			max_ = max(sum_, max_)
	print max_

find_max()


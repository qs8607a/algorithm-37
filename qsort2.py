import random
data = list()
for i in xrange(10000):
	data.append(random.randint(1,100))

def qsort(l, h):
	if l >= h:
		return

	j = l - 1
	#print 111, l, h, t, j, data
	for i in xrange(l, h):
		if data[i] <= t:
			j += 1
			tmp = data[j]
			data[j] = data[i]
			data[i] = tmp

	j += 1
	data[h] = data[j]
	data[j] = t

	qsort(l, j - 1)
	qsort(j + 1, h)

qsort(0, len(data) - 1)

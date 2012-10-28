import common
data = common.gen_rand_list(10000, 1, 100)

def qsort(l, h):
	if l >= h:
		return

	t = data[h]
	i = l
	j = h - 1


	while (True):
		while i <= h:
			if data[i] > t:
				break
			i += 1

		while j >= l:
			if data[j] < t:
				break
			j -= 1

		if i > j:
			break

		tmp = data[j]
		data[j] = data[i]
		data[i] = tmp

	j += 1
	data[h] = data[j]
	data[j] = t

	qsort(l, j - 1)
	qsort(j + 1, h)

qsort(0, len(data) - 1)

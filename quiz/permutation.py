
def Permutaion(array):
	if len(array) == 1:
		return [array]

	result = list()
	top =array.pop(0)
	for one_result in Permutaion(array):
		for j in xrange(len(one_result) + 1):
			copy_result = one_result[:]
			copy_result.insert(j, top)
			result.append(copy_result)
	array.insert(0, top)
	return result

print Permutaion([1,2,3,4])

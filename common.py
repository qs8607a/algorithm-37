import random

def gen_rand_list(n, l, u):
	data = list()
	for i in xrange(n):
		data.append(random.randint(l,u))
	return data

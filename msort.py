import common

data = common.gen_rand_list(6, 1, 100)

print data


def msort(l, u):
	if l >= u:
		return [data[l]]
	m = int((l + u) / 2)
	msort(l, m)
	msort(m + 1, u)
	merge(l, m, u)

def merge(l, m, u):
	i = l
	j = m + 1

	#print l, m, u, data[l:m+1], data[m+1: u+1]
	while(i != j and j != u + 1):
		if data[i] >= data[j]:
			data.insert(i, data[j])
			i += 1
			j += 1
			del data[j]
		else:
			i += 1
		#print "i:%d, j:%d" %(i,j), data[l:u + 1]

msort(0, len(data) - 1)
#print data

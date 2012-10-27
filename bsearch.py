s = [1,4,5,7,9,11,22,100,200]
s = [0, 10, 20, 30, 40, 50]

def bsearch(t):
	l = 0
	h = len(s) - 1
	while( l <= h ):
		m = int((l + h) / 2)
		if s[m] < t:
			l = m + 1
		elif s[m] > t:
			h = m - 1
		else:
			return m


print bsearch(40)

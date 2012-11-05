a  = [2,1,1,1,1,3, 10,1, 1, 1,2]

i = 0
j = len(a) - 1

sum1 = 0
sum2 = 0

while j > i:
	if sum1 >= sum2:
		sum2 += a[j]
		j -= 1
	else:
		sum1 += a[i]
		i += 1

print i,j

m = []
for x in range(5):
	r = input()
	r = r.split()
	for y in range(5):
		if r[y] == '1':
			i = x
			j = y

print(abs(2 - i) + abs(2 - j))
from math import ceil

n, k = [int(x) for x in input().split()]
middle = ceil(n / 2)

if k <= middle:
    print(((k - 1) * 2) + 1)
else:
    print((k - middle) * 2)
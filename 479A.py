import operator

a = int(input())
b = int(input())
c = int(input())

ops = [operator.add, operator.mul]
res = 0
for ox in ops:
    for oy in ops:
        tmp = max(oy(ox(a, b), c), oy(a, ox(b, c)))
        if (tmp > res): res = tmp

print(res)
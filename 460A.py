n, m = [int(x) for x in input().split()]

day = 0
while True:
    if n == 0:
        print(day)
        break
    day += 1
    n -= 1
    if day % m == 0: n += 1

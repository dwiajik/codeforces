n, t = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

i = 0
while True:
    i = i + a[i]
    if t == i + 1: 
        print("YES")
        break
    if t < i + 1:
        print("NO")
        break
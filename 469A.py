n = int(input())
x = input().split()
p = int(x.pop(0))
y = input().split()
q = int(y.pop(0))

print("I become the guy." if len(set(x + y)) == n else "Oh, my keyboard!")
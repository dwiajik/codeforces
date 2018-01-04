n = int(input())

def is_composite(n):
    for i in range(n - 2):
        if n % (i + 2) == 0: return True
    return False

for i in range(n - 2):
    x = i + 2
    y = n - x
    if is_composite(x) and is_composite(y):
        print("{} {}".format(x, y))
        break
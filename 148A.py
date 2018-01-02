k = input()
l = input()
m = input()
n = input()
d = input()
damaged = 0

for i in range(int(d)):
    if (i + 1) % int(k) == 0 or\
        (i + 1) % int(l) == 0 or\
        (i + 1) % int(m) == 0 or\
        (i + 1) % int(n) == 0:
        damaged = damaged + 1

print(damaged)
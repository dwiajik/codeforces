n = int(input())
plist = input().split()

friends = [0 for i in range(n)]

for index, pi in enumerate(plist):
    pi = int(pi)
    friends[pi - 1] = index + 1

print(" ".join(str(f) for f in friends))
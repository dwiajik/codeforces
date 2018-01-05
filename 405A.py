n = int(input())
cubes = [int(a) for a in input().split()]
print(" ".join([str(a) for a in sorted(cubes)]))
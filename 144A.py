n = int(input())
soldiers = [int(x) for x in input().split()]

min_index = n - 1 - soldiers[::-1].index(min(soldiers))
max_index = soldiers.index(max(soldiers))

steps = max_index + (n - 1 - min_index)

print(steps if min_index > max_index else steps - 1)
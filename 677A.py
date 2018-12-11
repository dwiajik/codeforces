n, h = [int(i) for i in input().split()]
heights = [int(h) for h in input().split()]

width = 0
for height in heights:
  if height > h:
    width += 2
  else:
    width += 1

print(width)

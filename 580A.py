n = input()
a = input().split(" ")

maxlength = 1
length = 1
prevai = None
for ai in a:
  ai = int(ai)
  if (prevai == None or prevai > ai):
    length = 1
  else:
    length = length + 1
    if (length > maxlength):
      maxlength = length
  prevai = ai

print(maxlength)
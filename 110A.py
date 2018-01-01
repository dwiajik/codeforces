import sys

number = input()

count = 0
for digit in number:
  if digit == "4" or digit == "7":
    count = count + 1

for digit in str(count):
  if digit != "4" and digit != "7":
    print("NO")
    sys.exit()

print("YES")
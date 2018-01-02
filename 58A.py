import sys
s = input()
i = 0
hello = "hello"
for l in s:
    if l == hello[i]:
        i = i + 1
        if (i == 5):
            print("YES")
            sys.exit()

print("NO")
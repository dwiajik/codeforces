input = input()
input = input.split()
k = int(input[0])
n = int(input[1])
w = int(input[2])

pay = 0

for i in range(w):
    pay = pay + (i + 1) * k

print( pay - n if (pay - n) > 0 else 0)
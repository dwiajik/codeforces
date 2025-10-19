t = input()

results = []
for i in range(int(t)):
    a, b = input().split()
    int_a = int(a)
    int_b = int(b)
    modulo = int_a % int_b
    if modulo > 0:
        num_moves = int_b - modulo
        results.append(num_moves)
    else:
        results.append("0")
for r in results:
    print(r)

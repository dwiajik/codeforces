n, t = input().split()
seq = list(input())

for i in range(int(t)):
    switchs = []
    for j in range(int(n) - 1):
        if seq[j] == 'B' and seq[j + 1] == 'G':
            switchs.append(j)
    for switch in switchs:
        seq[switch], seq[switch + 1] = seq[switch + 1], seq[switch]

print(''.join(seq))
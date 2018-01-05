n = int(input())

uniforms = []
for i in range(n):
    uniforms.append([int(x) for x in input().split()])

result = 0
for i in range(n):
    for j in range(i + 1, n):
        if uniforms[i][0] == uniforms[j][1]: result += 1
        if uniforms[i][1] == uniforms[j][0]: result += 1

print(result)
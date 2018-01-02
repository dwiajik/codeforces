n = int(input())

resultant = [0, 0, 0]
for i in range(n):
        numbers = input().split()
        resultant[0] += int(numbers[0])
        resultant[1] += int(numbers[1])
        resultant[2] += int(numbers[2])

for num in resultant:
        if num != 0:
                print('NO')
                exit()
print('YES')
def isLucky(number):
    number = str(number)
    for x in number:
        if x != '4' and x != '7':
            return False
    return True

result = 'NO'
number = input()
number = int(number)
for i in range(int(number)):
    if (isLucky(i + 1)):
        if (number % (i + 1) == 0):
            result = 'YES'
            break

print(result)
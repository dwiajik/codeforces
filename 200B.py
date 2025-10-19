n = input()
drinks = input().split()

total = 0
for drink in drinks:
    total = total + int(float(drink))

print(total/len(drinks))
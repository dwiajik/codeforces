n = int(input())

last_magnet = "00"
count = 0
for i in range(n):
    a = input()
    if a != last_magnet: count += 1
    last_magnet = a
print(count)
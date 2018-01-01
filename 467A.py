n = input()
result = 0
for i in range(int(n)):
  room = input()
  room = room.split()
  if int(room[1]) - int(room[0]) >= 2:
    result = result + 1

print(result)
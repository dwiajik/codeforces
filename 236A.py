username = input()
letter = []
for l in username:
  if l not in letter:
    letter.append(l)

if len(letter) % 2 == 0:
  print("CHAT WITH HER!")
else:
  print("IGNORE HIM!")
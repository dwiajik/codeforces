n = input()
answers = input().split()

result = "EASY"
for answer in answers:
    if answer == "1":
        result = "HARD"
        break
print(result)
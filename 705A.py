n = input()

hate = "I hate"
love = "I love"

feelings = []
for i in range(int(n)):
    if i % 2 == 0:
        feelings.append(hate)
    else:
        feelings.append(love)

print(" that ".join(feelings) + " it")
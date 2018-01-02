str = input()
numList = str.split("+")
numList.sort()
newStr = ""
for c in numList:
    newStr += c + "+"

print(newStr[0:-1])
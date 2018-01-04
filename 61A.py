x = input()
y = input()

result = ""
for i in range(len(x)):
    if x[i] == y[i]: result = result + "0"
    else: result = result + "1"

print(result)
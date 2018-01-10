s = input()[1:-1].split(", ")
print(0 if "" in s else len(set(s)))
n, k = input().split()
result = n
for i in range(int(k)):
    last_digit = result[-1]
    result_int = int(float(result))
    if last_digit == "0":
        result = str(int(result_int / 10))
    else:
        result = str(int(result_int - 1))
print(result)
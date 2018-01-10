candle, b = [int(x) for x in input().split()]

hours = 0
burnt_out = 0
while True:
    if candle <= 0:
        break
    hours += candle
    burnt_out += candle
    candle = int((burnt_out) / b)
    burnt_out = burnt_out % b

print(hours)
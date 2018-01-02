n = input()
coins = input().split()
coins = list(map(int, coins))
coins.sort(reverse=True)
avg = sum(coins)/2

count = 0
ownCoins = 0

for coin in coins:
    ownCoins += coin
    count += 1
    if ownCoins > avg:
        break

print(count)
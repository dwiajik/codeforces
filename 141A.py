guest = input()
host = input()
suffled = input()

print('YES' if sorted(guest + host) == sorted(suffled) else 'NO')
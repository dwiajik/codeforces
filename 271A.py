year = int(input())

while True:
    year += 1
    yearStr = str(year)
    if len(set(yearStr)) == len(yearStr):
        print(yearStr)
        exit()

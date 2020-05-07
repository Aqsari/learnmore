deposit = int(input())

years = 0
while 50000 < deposit < 700000:
    years += 1
    interest = deposit * 7.1 / 100
    deposit = deposit + interest

print(years)

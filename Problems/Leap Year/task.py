year = int(input())

# print(year % 4)
# print(year % 100)
# print(year % 400)
if 1900 <= year <= 3000:
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            print("Leap")
        else:
            print("Ordinary")
    else:
        print("Ordinary")

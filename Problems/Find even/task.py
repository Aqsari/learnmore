number = int(input())

loop = 1
if 1 < number < 200:
    while loop < number:
        if loop % 2 == 0:
            print(loop)
        loop += 1

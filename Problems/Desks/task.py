number1 = int(input())
number2 = int(input())
number3 = int(input())

number1_last = number1 % 2
number2_last = number2 % 2
number3_last = number3 % 2

number = int(number1 / 2) + number1_last + int(number2 / 2) + number2_last + int(number3 / 2) + number3_last

print(number)
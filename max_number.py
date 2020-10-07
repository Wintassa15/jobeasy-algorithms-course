#Find max number from 3 values, entered manually from a keyboard
number1 = input('enter the first number:')
number2 = input("enter the second number:")
number3 = input('enter the third number:')
if number1 > number2 and number1 > number3:
    max_number = number1
elif number2 > number1 and number2 > number3:
    max_number = number2
else:
    max_number = number3
print(max_number)
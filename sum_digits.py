#Rewrite a program with any number of digits.
#  Instead of  3 digits, you should sum digits up from n digits number,
#  Where User enter n manually. n > 0

number = int(input('enter any digits number '))
result = 0
if number > 0:
    for digits in str(number):
        result += int(digits)
    print(result)
else:
    print('enter a positive number')

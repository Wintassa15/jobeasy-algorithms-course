#Count odd and even numbers.  Count odd and even digits of the whole number. E.g, if entered number 34560, then 3 digits will be even (4, 6, and 0)  and  2 odd digits (3 and 5).
number = input('enter a whole number')
even_number = 0
odd_number = 0
for digit in number:
    if int(digit ) % 2 == 0:
        even_number += 1
    else:
        odd_number += 1
print("even numbers are :" + str(even_number) + " odd numbers are:" + str(odd_number))


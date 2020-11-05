# Rules are: (1) the letters are adjacent in the English alphabet, and (2) each letter occurs only once.
#
# For example:
# solve("abc") = True, because it contains a,b,c
# solve("abd") = False, because a, b, d are not consecutive/adjacent in the alphabet, and c is missing.
# solve("dabc") = True, because it contains a, b, c, d
# solve("abbc") = False, because b does not occur once.
# solve("v") = True

def consecutive_letters(st):
    a = ''.join(sorted(st))
    if a in 'abcdefghijklmnopqrstuvwxyz':
        return True
    else:
        return False


print(consecutive_letters('abbc'))


# Given a string of digits confirm whether the sum of all the individual even digits are greater than the sum of all
# the individual odd digits. Always a string of numbers will be given.
#
# If the sum of even numbers is greater than the odd numbers return: "Even is greater than Odd"
#
# If the sum of odd numbers is greater than the sum of even numbers return: "Odd is greater than Even"
#
# If the total of both even and odd numbers are identical return: "Even and Odd are the same"
# test.assert_equals(even_or_odd('12'), 'Even is greater than Odd')
#     test.assert_equals(even_or_odd('123'), 'Odd is greater than Even')
#     test.assert_equals(even_or_odd('112'), 'Even and Odd are the same')

def even_odd(number):
    odd_sum = 0
    even_sum = 0

    for i in number:
        if int(i) % 2 == 0:
            even_sum += int(i)
        else:
            odd_sum += int(i)
    if even_sum > odd_sum:
        return "even is greater than odd"
    elif odd_sum > even_sum:
        return "odd is greater than even"
    else:
        return "even and odd are the same"


print(even_odd('12'))


#you are asked to square every digit of a number and concatenate them.
#For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

def square_numbers(num):
    squares = ''
    for x in str(num):
        squares += str(pow(int(x),2))
    return int(squares)


print(square_numbers(9119))






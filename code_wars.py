# When it's spring Japanese cherries blossom, it's called "sakura" and it's admired a lot. The petals start to fall in late April.
#
# Suppose that the falling speed of a petal is 5 centimeters per second (5 cm/s), and it takes 80 seconds for the petal to reach the ground from a certain branch.
#
# Write a function that receives the speed (in cm/s) of a petal as input, and returns the time it takes for that petal to reach the ground from the same branch.
#
# Notes:
#
# The movement of the petal is quite complicated, so in this case we can see the velocity as a constant during its falling.
# Pay attention to the data types.
# If the initial velocity is non-positive, the return value should be

# test.assert_approx_equals(sakura_fall(5), 80)
# test.assert_approx_equals(sakura_fall(10), 40)
# test.assert_approx_equals(sakura_fall(-1), 0)

def sakura_fall(v):
    if v < 0:
        return 0
    else:
        time = 400 / v
        return time
sakura_fall(10)


# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
#
# For example:
#
# summation(2) -> 3
# 1 + 2
#
# summation(8) -> 36
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8

#sample tests
# test.assert_equals(summation(1), 1)
#     test.assert_equals(summation(8), 36)
#     test.assert_equals(summation(22), 253)
#     test.assert_equals(summation(100), 5050)
#     test.assert_equals(summation(213), 22791)

def summation(num):
    if num < 0:
        return False
    else:
        total = 0
        for number in range(1, num+1):
            total += number
        return total
print(summation(100))

# Given two integers a and b, which can be positive or negative, find the sum of all the numbers between including them too and return it. If the two numbers are equal return a or b.
#
# Note: a and b are not ordered!
#
# Examples
#
# get_sum(1, 0) == 1   // 1 + 0 = 1
# get_sum(1, 2) == 3   // 1 + 2 = 3
# get_sum(0, 1) == 1   // 0 + 1 = 1
# get_sum(1, 1) == 1   // 1 Since both are same
# get_sum(-1, 0) == -1 // -1 + 0 = -1
# get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2

def get_sum(a,b):
    if a == b:
        return a
    else:
        max_number = max(a, b)
        min_number = min(a, b)
        sum_numbers = sum(range(min_number, max_number + 1))
        return sum_numbers
print(get_sum(1, 2))




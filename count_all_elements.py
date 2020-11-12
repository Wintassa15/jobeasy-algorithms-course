# Write a recursive function to count all the elements in a list (divide and rule).
from math import floor
from random import randint

length = int(input('enter number of elements'))
list = []

for _ in range(length):
    list.append(randint(1, 10))
print(list)


def count_all_elements(array):
    mid = floor(length / 2)
    left = array[:mid]
    right = array[mid:]

    result_1 = array.count(left)
    result_2 = array.count(right)
    return result_1 + result_2

    # for i in left:
    #    result_1 = left.count(i)
    # for j in right:
    #    result_2 = right.count(i)
    # return count_all_elements(result_1) + count_all_elements(result_2)


print(count_all_elements([list]))



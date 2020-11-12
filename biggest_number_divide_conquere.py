# Find the biggest number in the list (divide and rule).
from math import floor
from random import randint

length = int(input('enter number of items'))
list_items = []
#
for _ in range(length):
    list_items.append(randint(0, 20))
print(list_items)


#
#
def biggest_number(array):
    mid = floor(length / 2)
    left = array[:mid]
    right = array[mid:]
    max_1 = max(left)
    max_2 = max(right)
    return max(max_1, max_2)


#
#
print(biggest_number(list_items))

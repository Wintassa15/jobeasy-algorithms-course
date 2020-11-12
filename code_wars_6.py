# Given an array of integers , Find the maximum product obtained from multiplying 2 adjacent numbers in the array.
# Test.it("Positive numbers")
# Test.assert_equals(adjacent_element_product([5, 8]), 40)
# Test.assert_equals(adjacent_element_product([1, 2, 3]), 6)
# Test.assert_equals(adjacent_element_product([1, 5, 10, 9]), 90)
# Test.assert_equals(adjacent_element_product([4, 12, 3, 1, 5]), 48)
# Test.assert_equals(adjacent_element_product([5, 1, 2, 3, 1, 4]), 6)
#
# Test.it("Both positive and negative values")
# Test.assert_equals(adjacent_element_product([3, 6, -2, -5, 7, 3]), 21)
# Test.assert_equals(adjacent_element_product([9, 5, 10, 2, 24, -1, -48]), 50)
# Test.assert_equals(adjacent_element_product([5, 6, -4, 2, 3, 2, -23]), 30)
# Test.assert_equals(adjacent_element_product([-23, 4, -5, 99, -27, 329, -2, 7, -921]), -14)


def element_product(array):
    result = []
    for i in range(0, len(array) - 1):
        result.append(array[i] * array[i + 1])
    return max(result)


print(element_product([9, 5, 10, 2, 24, -1, -48]))


#Given an array of integers, find the one that appears an odd number of times.

# Sample Tests:
# test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
# test.assert_equals(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1);
# test.assert_equals(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5);
# test.assert_equals(find_it([10]), 10);
# test.assert_equals(find_it([1,1,1,1,1,1,10,1,1,1,1]), 10);
# test.assert_equals(find_it([5,4,3,2,1,5,4,3,2,10,10]), 1);

def odd_number_of_times(array):
    list_odd_appearance= []
    for i in array:
        result = array.count(i)
        if result % 2 != 0 and i not in list_odd_appearance:
            list_odd_appearance.append(i)
    return list_odd_appearance


print(odd_number_of_times([1,1,1,1,1,1,10,1,1,1,1]))
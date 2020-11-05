# When given a list of elements find the two lowest elements. They can be equal to each other or different.

def lowest_elements(list1):
    smallest = list1[0]
    smallest_2 = None
    for item in list1:
        if item < smallest:
            smallest_2 = smallest
            smallest = item
        elif smallest_2 == None or smallest_2 < item:
            largest2 = item
    return {
        'first minimum': smallest,
        'second minimum': smallest_2
    }


print(lowest_elements([8, 3, 2, 4, ]))

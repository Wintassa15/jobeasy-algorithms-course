# When given a list, the program should return a list of all the elements that are below the arithmetical mean of the
# original list.  The arithmetical mean is the sum of all elements divided by the number of elements.

def arithmetical_mean(list):
    total = 0
    n = len(list)
    new_list = []
    for i in list:
        total += i
        # i += 1
        mean = total / n
    for i in list:
        if i < mean:
            new_list.append(i)
    return new_list


print(arithmetical_mean([1, 2, 30, 4, 5, 9, 15]))

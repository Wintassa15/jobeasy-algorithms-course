#Write a Python program to remove duplicates from a list.
def remove_duplicates(list):
    new_list = []
    for number in list:
        if number not in new_list:
            new_list.append(number)
    return new_list


print(remove_duplicates([1,1,2,2,3,3,4]))

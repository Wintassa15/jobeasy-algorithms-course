# Task
#
# Given a list lst and a number N, create a new list that contains each number of lst at most N times without
# reordering. For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,
# 2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
#
# Example
#
#   delete_nth ([1,1,1,1],2) # return [1,1]
#
#   delete_nth ([20,37,20,21],1) # return [20,37,21]


def delete_nth(order,max_e):
    new_list = []
    count = 0
    for i in order:
        if i in new_list:
            count += 1
            if count != max_e:
                new_list.append(i)

        else:
            new_list.append(i)
    return new_list


print(delete_nth([20,37,20,21],1))



# Write a function named setAlarm which receives two parameters. The first parameter, employed, is true whenever you are employed and the second parameter, vacation is true whenever you are on vacation.
#
# The function should return true if you are employed and not on vacation (because these are the circumstances under which you need to set an alarm). It should return false otherwise. Examples:
#
# setAlarm(true, true) -> false
# setAlarm(false, true) -> false
# setAlarm(false, false) -> false
# setAlarm(true, false) -> true

def set_alarm(employed, vacation):
    if employed == 1 and vacation == 0:
        return True
    else:
        return False


# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word
# within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case,
# also often referred to as Pascal case).
#
# Examples
#
# to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"
#
# to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"

def to_camel_case(text):
    return text.capitalize().replace('-','_')


to_camel_case('the-stealth-warrior')

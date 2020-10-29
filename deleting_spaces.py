# Enter an irregular string (that means it may have space at the beginning of a string, at the end of the string,
# and words may be separated by several spaces). Make the string regular (delete all spaces at the beginning and end
# of the string, leave one space separating words).

def delete_spaces(string):
    result = ' '.join(string.split())
    return result


print(delete_spaces(input('enter an irregular spaces:')))

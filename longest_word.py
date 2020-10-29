# Enter a string of words separated by spaces. Find the longest word. (split / join methods)
def longest_word(string):
    new_string = string.split(' ')
    print(new_string)
    result = ''
    for word in new_string:
        if len(word) > len(result):
            result = word
    return result


print(longest_word('This is python'))

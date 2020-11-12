# There are two lists that have different length. First has keys and the second has values.
# Create a function, which creates a dictionary of keys and values.
# If the is not enough values to match each key, this key should have value equal to None.
# If the is not enough keys to match each value, this value should be ignored.
def match_keys_and_values(keys,values):
    d = {}
    for key in keys:
        for value in values:
            if len(keys) == len(values):
                d[key] = value
                values.remove(value)
            elif len(keys) > len(values):
                for key in range(len(values),len(keys)):
                    d[key] = 'none'

    return d


print(match_keys_and_values(['winta','Adam','Henok','Haben','Heaven','Heri'],['It','Doctor','Pharmacist','Accountant']))
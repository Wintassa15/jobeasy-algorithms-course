# Zeros not for Heros
# Numbers ending with zeros are boring. They might be fun in your world, but not here. Get rid of them. Only the ending ones.
def drop_zeros(number):
    if number == 0:
        print('it is just zero')
    else:
        num = number.strip('0')
    return num

print(drop_zeros(input('enter a number with zeros')))

# or
def remove_zeros(num):
    while num % 10 == 0:
        num //= 10
    return num
print(remove_zeros(int(input('enter a number'))))





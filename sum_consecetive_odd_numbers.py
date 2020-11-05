# Given the triangle of consecutive odd numbers:
#          	     1
#             3      5
#         7      9	  11
#    13	 15    17    19
# 21    23    25     27     29
# ...
# Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:
#
# row_sum_odd_numbers(1); # 1
# row_sum_odd_numbers(2); # 3 + 5 = 8
# row_sum_odd_numbers(3); # 7 + 9 + 11 = 27
# row_sum_odd_numbers(3); # 13 + 15 + 17 + 19 = 64

def sum_off_odd_numbers(n):
    first_digit = n * (n - 1) + 1
    total = 0
    for i in range(n):
        total += first_digit
        first_digit += 2
    return total

print(sum_off_odd_numbers(19))


# example with import math

import math

def multiply_numbers(*args):
    return math.prod(args)

multiply_numbers(5, 3, 10)

# example with no imports

def multiply_numbers_2(*args):
    answer = 1
    for num in args:
        answer *= num
    return answer

multiply_numbers_2(5, 3, 10)
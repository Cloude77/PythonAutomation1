import math


def calc_factorial(num):
    if type(num) is not int:
        raise TypeError("Number must be integer")
    if num <= 0:
        raise ValueError("Number must be positive")
    # 10! == 10 * 9 * 8 * 7...* 1
    if num == 1:
        return 1  # end factorial
    return calc_factorial(num - 1) * num


# calc_factorial('abc') # TypeError: Number must be integer
print(calc_factorial(10))  # 3628800
print(math.factorial(10))  # function works correctly

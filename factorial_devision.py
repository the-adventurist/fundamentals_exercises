import functools


def factorial_and_order_division(n1, n2):
    first_factorial = functools.reduce(lambda x, y: x * y, range(n1, 0, -1))
    second_factorial = functools.reduce(lambda x, y: x * y, range(n2, 0, -1))
    result = f"{first_factorial / second_factorial:.2f}"
    return result


print(factorial_and_order_division(int(input()), int(input())))

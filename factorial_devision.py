def factorial_division(n):
    if n == 1:
        return 1
    else:
        return n * factorial_division(n - 1)


def order_division(n1, n2):
    factorial_n1 = factorial_division(n1)
    factorial_n2 = factorial_division(n2)
    result_order_division = factorial_n1 / factorial_n2
    return f'{result_order_division:.2f}'


print(order_division(int(input()), int(input())))

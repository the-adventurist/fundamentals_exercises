import functools

n1 = 5

first_factorial = functools.reduce(lambda x, y: x * y, range(n1, 0, -1))
print(first_factorial)

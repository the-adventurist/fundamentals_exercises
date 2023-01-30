def is_even(x):
    return x % 2 == 0


numbers = [int(x) for x in input().split()]
filtered_numbers = filter(is_even, numbers)
print(list(filtered_numbers))

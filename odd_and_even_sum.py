def extractor(n):
    sum_odd = 0
    sum_even = 0
    for digit in n:
        digit = int(digit)
        if digit % 2 == 0:
            sum_even += digit
        else:
            sum_odd += digit
    return sum_even, sum_odd


number_as_str = input()
result = extractor(number_as_str)
print(f'Odd sum = {result[1]}, Even sum = {result[0]}')

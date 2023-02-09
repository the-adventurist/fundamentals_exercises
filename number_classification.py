number_sequence = [int(x) for x in input().split(', ')]

positive = []
negative = []
even = []
odd = []

for num in number_sequence:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
    if num < 0:
        negative.append(num)
    else:
        positive.append(num)

print(f'Positive: {", ".join([str(x) for x in positive])}')
print(f'Negative: {", ".join([str(x) for x in negative])}')
print(f'Even: {", ".join([str(x) for x in even])}')
print(f'Odd: {", ".join([str(x) for x in odd])}')

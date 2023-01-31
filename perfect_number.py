def definer_of_perfect_number(n):
    sum_proper_divisors = 0
    for d in range(1, n):
        if n % d == 0:
            sum_proper_divisors += d
    if sum_proper_divisors == n:
        return "We have a perfect number!"
    return "It's not so perfect."


print(definer_of_perfect_number(int(input())))

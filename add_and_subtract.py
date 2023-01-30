def sum_numbers(first, second):
    return first + second


def subtract(result, third):
    return result - third


def add_and_subtract(first, second, third):
    result_of_addition = sum_numbers(first, second)
    result_of_subtraction = subtract(result_of_addition, third)
    return result_of_subtraction


first_number = int(input())
second_number = int(input())
third_number = int(input())


print(add_and_subtract(first_number, second_number, third_number))

origin_string = input()
numbers_list = []
non_numbers_list = []

for element in origin_string:
    if element.isdigit():
        numbers_list.append(element)
    else:
        non_numbers_list.append(element)

take_list = []
skip_list = []

for index in range(len(numbers_list)):
    if index % 2 == 0:
        take_list.append(int(numbers_list[index]))
    else:
        skip_list.append(int(numbers_list[index]))

result = ''
number_of_iteration = len(take_list)
for _ in range(number_of_iteration):
    taken_letters = take_list.pop(0)
    result += ''.join([x for x in non_numbers_list[:taken_letters]])
    non_numbers_list = non_numbers_list[taken_letters + 1:]
    skipped_letters = skip_list.pop(0)
    non_numbers_list = non_numbers_list[skipped_letters + 1:]

print(result)

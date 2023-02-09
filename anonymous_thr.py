import time
start_time = time.perf_counter()


from functools import reduce


def merge_action(start, end, sequence):
    modification = list(reduce(lambda x, y: x + y, strings_sequence[start_i: end_i + 1]))
    modification = ''.join(modification)
    return modification


def correcting_boundaries(start, end, list_):
    if 0 <= start < end < len(list_):
        return start, end
    if end >= len(list_):
        end = len(list_) - 1
    if 0 <= start < end < len(list_):
        return start, end
    return 0, 0

strings_sequence = input().split()

attack = input()
while attack != '3:1':
    attack_args = attack.split()
    type_attack = attack_args[0]
    if type_attack == 'merge':
        start_i = int(attack_args[1])
        end_i = int(attack_args[2])
        start_i, end_i = correcting_boundaries(start_i, end_i, strings_sequence)
        if start_i == 0 and end_i == 0:
            continue
        if start_i == 0:
            last_part = strings_sequence[end_i + 1:]
            modified_part = merge_action(start_i, end_i, strings_sequence)
            strings_sequence = [modified_part]
            strings_sequence.extend(last_part)
        elif end_i == len(strings_sequence) - 1:
            beginning_part = strings_sequence[:start_i]
            modified_part = merge_action(start_i, end_i, strings_sequence)
            strings_sequence = beginning_part
            strings_sequence.append(modified_part)
        elif start_i > 0:
            beginning_part = strings_sequence[:start_i]
            modified_part = merge_action(start_i, end_i, strings_sequence)
            ending_part = strings_sequence[end_i + 1:]
            beginning_part.append(modified_part)
            beginning_part.extend(ending_part)
            strings_sequence = beginning_part
    else:
        element_at_this_index = int(attack_args[1])
        beginning_part_string_sequence = strings_sequence[: element_at_this_index]
        last_part_string_sequence = strings_sequence[element_at_this_index + 1:]
        to_number_of_parts = int(attack_args[2])
        this_element = strings_sequence[element_at_this_index]
        insert_sequence = []
        size_part = len(this_element) / to_number_of_parts
        additional_elements = []
        if not size_part.is_integer():
            for part in range(0, to_number_of_parts * int(size_part), int(size_part)):
                if part < to_number_of_parts * int(size_part) - int(size_part):
                    part_to_add = this_element[part:int(size_part) + part]
                    additional_elements.append(part_to_add)
                else:
                    part_to_add = this_element[part:]
                    additional_elements.append(part_to_add)
        else:
            for part in range(0, to_number_of_parts * int(size_part), int(size_part)):
                part_to_add = this_element[part:int(size_part) + part]
                additional_elements.append(part_to_add)
        beginning_part_string_sequence.extend(additional_elements)
        beginning_part_string_sequence.extend(last_part_string_sequence)
        strings_sequence = beginning_part_string_sequence
    attack = input()

print(' '.join(strings_sequence))


end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"The execution time is: {execution_time}")
def correcting_boundaries(start, end, list_):
    if start < 0:
        start = 0
    if 0 <= start < end < len(list_):
        return start, end
    if end >= len(list_):
        end = len(list_) - 1
    if 0 <= start < end < len(list_):
        return start, end
    return 0, 0


strings = input().split()

attack = input()

while attack != '3:1':
    attack_args = attack.split()
    type_attack = attack_args[0]
    if type_attack == 'merge':
        start_i = int(attack_args[1])
        end_i = int(attack_args[2])
        start_i, end_i = correcting_boundaries(start_i, end_i, strings)
        if not start_i and not end_i:
            attack = input()
            continue
        merged_element = ''
        new_strings_sequence = []
        for element in range(len(strings)):
            if element < start_i:
                new_strings_sequence.append(strings[element])
            elif start_i <= element <= end_i:
                merged_element += strings[element]
            if element == end_i:
                new_strings_sequence.append(merged_element)
            elif element > end_i:
                new_strings_sequence.append(strings[element])
        strings = new_strings_sequence
    else:
        chunks = []
        element_to_division_index = int(attack_args[1])
        element_to_division = strings[element_to_division_index]
        chunks_number = int(attack_args[2])
        size_chunk = len(element_to_division) // chunks_number
        for current_chunk in range(0, chunks_number * size_chunk, size_chunk):
            if current_chunk < (chunks_number * size_chunk) - size_chunk:
                chunks.append(element_to_division[current_chunk: size_chunk + current_chunk])
            else:
                chunks.append(element_to_division[current_chunk:])
        strings.pop(element_to_division_index)
        for chunk in range(len(chunks) -1, -1, -1):
            strings.insert(element_to_division_index, chunks[chunk])

    attack = input()

print(' '.join(strings))

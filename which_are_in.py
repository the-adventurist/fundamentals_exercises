substrings = input().split(', ')
strings = input().split(', ')
result_strings = []

for substring in substrings:
    for string in strings:
        if substring in string:
            result_strings.append(substring)
            continue

print(result_strings)

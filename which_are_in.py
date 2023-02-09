substrings = input().split(', ')
strings = input()
result_strings = []

for substring in substrings:
    if substring in strings:
        result_strings.append(substring)
print(result_strings)

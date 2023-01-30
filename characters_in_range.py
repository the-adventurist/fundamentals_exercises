def filler(start, final):
    result = ''
    for i in range(ord(start) + 1, ord(final)):
        if i < ord(final) - 1:
            result += chr(i) + ' '
        else:
            result += chr(i)
    return result


start_letter = input()
final_letter = input()
print(filler(start_letter, final_letter))

encrypted_messages = input().split()
decrypted_messages = ''

for current_message in encrypted_messages:
    number_ascii = [n for n in current_message if n.isdigit()]
    number_code_for_ascii = int(''.join(number_ascii))
    letter = chr(number_code_for_ascii)
    current_message = [l for l in current_message if l.isalpha()]
    current_message.insert(0, letter)
    current_message[1], current_message[-1] = current_message[-1], current_message[1]
    current_message = ''.join(current_message)
    decrypted_messages += current_message + ' '
print(decrypted_messages)

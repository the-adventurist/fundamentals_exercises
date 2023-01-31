def password_validator(p):
    message = ''
    if not(6 <= len(p) <= 10):
        message += "Password must be between 6 and 10 characters" + "\n"
    if not p.isalnum():
        message += "Password must consist only of letters and digits" + "\n"
    counter = [+1 for i in p if i.isdigit()]
    if len(counter) < 2:
        message += "Password must have at least 2 digits"
    if message:
        return message
    return "Password is valid"


print(password_validator(input()))

def palindrome_checker(n):
    n = [x for x in n]
    if n == n[::-1]:
        return True
    return False


numbers = input().split(', ')
for num in numbers:
    print(palindrome_checker(num))

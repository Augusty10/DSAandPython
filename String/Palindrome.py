def is_palindrome(n):
    num = n
    result = 0

    while num > 0:
        digit = num % 10
        result = (result * 10) + digit
        num = num // 10

    return n == result

print(is_palindrome(1234))

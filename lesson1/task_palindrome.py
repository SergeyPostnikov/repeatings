def is_palindrome(s):
    return s == s[::-1]


if __name__ == '__main__':
    s = 'аргентинаманитнегра'
    print(is_palindrome(s))

# My Solution (same as book's with different syntax)


def is_palindrome(s):
    start, end = 0, len(s) - 1

    while start < end:
        while not s[start].isalnum() and start < end:
            start += 1
        while not s[end].isalnum() and start < end:
            end -= 1
        if s[start].lower() != s[end].lower():
            return False
        start += 1
        end -= 1
    return True


# Pythonic solution


def is_palindrome_pythonic(s):
    return all(a == b for a, b in zip(map(str.lower, filter(str.isalnum, s)),
                                      map(str.lower, filter(str.isalnum, reversed(s)))))


print(is_palindrome('racecar'), is_palindrome('A man, a plan, a canal, Panama!'), is_palindrome('NoT a Palindrome'))

def make_palindrome(input):
    if input != input[::-1]:
        return input + (input[:-1])[::-1]
    return input
def dec_to_bin(number):
    answer = ''
    while number != 0:
        if number % 2 == 0:
            answer += '0'
        else:
            answer += '1'
        number //= 2
    answer = answer[::-1]
    return answer

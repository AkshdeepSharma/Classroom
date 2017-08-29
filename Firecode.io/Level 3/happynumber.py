def is_happy_number(number):
    count = 0
    while number != 1 and count < 1000:
        vals_str = []
        vals_int = []
        for digit in str(number):
            vals_str.append(digit)
        for i in vals_str:
            vals_int.append(int(i) * int(i))
        number = sum(vals_int)
        count += 1
    if number == 1:
        return True
    return False

print(is_happy_number(12))
def is_power_of_four(number):
    binary = list(bin(number)[2:])
    binary = [int(x) for x in binary]
    if (len(binary) - 1) % 2 == 0:
        return True
    return False


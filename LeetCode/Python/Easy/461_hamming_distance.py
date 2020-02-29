def hamming_distance(x, y):
    bits = 0
    if x < y:
        x, y = y, x
    x, y = bin(x)[2:], bin(y)[2:]
    y = '0' * (len(x) - len(y)) + y
    for i in range(len(x)):
        if x[i] != y[i]:
            bits += 1
    return bits

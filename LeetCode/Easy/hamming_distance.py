def hamming_distance(x,y):
    if x > y:
        x, y = y, x
    x = bin(x)[2:]
    x = x[::-1]
    y = bin(y)[2:]
    bits = 0
    for i in range(len(y) - len(x)):
        x += '0'
    x = x[::-1]
    for i in reversed(range(len(x))):
        if x[i] != y[i]:
            bits += 1
    return bits


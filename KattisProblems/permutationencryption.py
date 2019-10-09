while True:
    inp = input().split()
    if inp == ["0"]:
        break
    permutation = list(map(int, inp[1:]))
    message = input()
    if len(message) % len(permutation) != 0:
        message += " " * (len(permutation) - (len(message) % len(permutation)))
    message = list(message)
    for i in range(len(message) // len(permutation)):
        code = {}
        for j in range(i * len(permutation), i * len(permutation) + len(permutation)):
            code[j] = message[j]
        for k in range(i * len(permutation), i * len(permutation) + len(permutation)):
            message[k] = code[permutation[k - i * len(permutation)] + i * len(permutation) - 1]
    print("'" + "".join(message) + "'")
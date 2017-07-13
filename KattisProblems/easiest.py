while True:
    N = int(input())
    n = 0
    sumOfDigits = 0
    newSumOfDigits = 0
    m = 10
    if N == 0:
        break
    for i in range(len(str(N))):
        sumOfDigits += int(str(N)[i])

    while sumOfDigits != newSumOfDigits:
        newSumOfDigits = 0
        m += 1
        for i in range(len(str(N * m))):
            newSumOfDigits += int(str(N * m)[i])
    print(m)

while True:
    numer, denom = map(int, input().split())
    if numer == 0 and denom == 0:
        break
    else:
        wholeNumber = numer // denom
        numer = numer - (denom * wholeNumber)
        print(wholeNumber, numer, "/", denom)

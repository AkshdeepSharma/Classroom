numberOfRings = int(input())
ringSizes = list(input().strip().split(' '))

def gcd (x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

for j in range(1, numberOfRings):
    output = int(ringSizes[0]) // int(ringSizes[j])
    if int(ringSizes[0]) % int(ringSizes[j]) == 0:
        print(str(int(output))+"/1")
    else:
        greatestCommonDenominator = gcd(int(ringSizes[0]), int(ringSizes[j]))
        numerator = int(ringSizes[0]) // int(greatestCommonDenominator)
        denominator = int(ringSizes[j]) // int(greatestCommonDenominator)
        print(str(numerator) + "/" + str(denominator))

from math import sqrt


def getSumOfDivisors(num):
    divisors = []
    for i in range(1, int(sqrt(num) + 1)):
        if num % i == 0:
            if num // i != i:
                divisors.append(i)
            divisors.append(num // i)
    return sum(divisors) - num


def main():
    try:
        while True:
            num = int(input())
            sumOfDivisors = getSumOfDivisors(num)
            if sumOfDivisors == num:
                print(f"{num} perfect")
            elif abs(sumOfDivisors - num) <= 2:
                print(f"{num} almost perfect")
            else:
                print(f"{num} not perfect")
    except EOFError:
        pass


if __name__ == '__main__':
    main()

import math
from collections import defaultdict


def find_all_factors_of_num(num):
    factors = defaultdict(int)
    factor = 2
    while factor ** 2 <= num:
        while num % factor == 0:
            factors[factor] += 1
            num /= factor
        factor += 1
    if num > 1:
        factors[num] += 1
    return factors


def find_PP(num, positive):
    factors = find_all_factors_of_num(num)
    max_pp = int(math.log(num, 2))
    while max_pp >= 1:
        found = True
        for factor in factors.values():
            if factor % max_pp != 0:
                found = False
                break
        if (positive and found) or (not positive and found and max_pp % 2 == 1):
            break
        max_pp -= 1
    return max_pp


def main():
    num = int(input())
    while num != 0:
        positive = True
        if num < 0:
            num *= -1
            positive = False
        print(find_PP(num, positive))
        num = int(input())


if __name__ == '__main__':
    main()

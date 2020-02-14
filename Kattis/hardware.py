def calculateDigits(addresses):
    digits = [0] * 10
    for num in addresses:
        for c in num:
            digits[int(c)] += 1
    return digits, sum(digits)


def main():
    orders = int(input())
    for _ in range(orders):
        addresses = []
        street_name = input()
        num_addresses = input().split()
        while len(addresses) < int(num_addresses[0]):
            numbers = input().split()
            if numbers[0] != "+":
                addresses.append(numbers[0])
                continue
            for i in range(int(numbers[1]), int(numbers[2]) + 1, int(numbers[3])):
                addresses.append(str(i))
        digits, total = calculateDigits(addresses)
        print(street_name)
        print(" ".join(num_addresses))
        for i in range(len(digits)):
            print("Make " + str(digits[i]) + " digit " + str(i))
        if total == 1:
            print("In total 1 digit")
        else:
            print("In total " + str(total) + " digits")


if __name__ == "__main__":
    main()

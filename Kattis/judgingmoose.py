def moose(left, right):
    if left == right == 0:
        return "Not a moose"
    elif left == right:
        return "Even " + str(left * 2)
    else:
        return "Odd " + str(max(left, right) * 2)


def main():
    left, right = map(int, input().split())
    print(moose(left, right))


if __name__ == '__main__':
    main()

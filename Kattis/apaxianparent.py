def get_name(Y, P):
    vowels = {"a", "e", "i", "o", "u"}
    if Y[-2:] == "ex":
        return Y + P
    elif Y[-1] in vowels:
        return Y[:-1] + "ex" + P
    else:
        return Y + "ex" + P


def main():
    Y, P = input().split()
    print(get_name(Y, P))


if __name__ == '__main__':
    main()

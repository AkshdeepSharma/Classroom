from math import sqrt


def decode_message(message):
    square = int(sqrt(len(message)))
    decoded = []
    for i in range(square - 1, -1, -1):
        for j in range(i, len(message), square):
            decoded.append(message[j])
    return "".join(decoded)


def main():
    T = int(input())
    for _ in range(T):
        message = input()
        print(decode_message(message))


if __name__ == '__main__':
    main()

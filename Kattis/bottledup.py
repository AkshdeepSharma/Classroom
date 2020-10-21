def numBottles(s, v1, v2):
    num_v1 = num_v2 = 0
    for i in range(s//v2 + 1):
        if (s - v2 * i) % v1 == 0:
            num_v1 = (s - v2 * i) // v1
            num_v2 = i
            return f"{num_v1} {num_v2}"
    return "Impossible"


def main():
    s, v1, v2 = map(int, input().split())
    print(numBottles(s, v1, v2))


if __name__ == "__main__":
    main()

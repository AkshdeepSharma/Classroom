def findFinalScores(s, d):
    if s < d or (s + d) % 2 != 0:
        return "impossible", ""
    a = (s + d) // 2
    b = s - a
    return a, b


def main():
    num_cases = int(input())
    for _ in range(num_cases):
        s, d = map(int, input().split())
        a, b = findFinalScores(s, d)
        print(str(a) + " " + str(b))


if __name__ == "__main__":
    main()

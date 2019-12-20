def main():
    N = int(input())
    superlag_time, regular_time = 0, 0
    for _ in range(N):
        SL_time, R_time = map(int, input().split())
        superlag_time += SL_time * 60
        regular_time += R_time
    ratio = regular_time / superlag_time
    if ratio <= 1:
        print("measurement error")
    else:
        print(round(ratio, 9))


if __name__ == "__main__":
    main()

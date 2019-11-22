import math


def main():
    try:
        dp = [0] * 1000001
        dp[0] = 1
        highest_calculated = 1
        while True:
            num = int(input())
            if dp[num] == 0:
                i = highest_calculated
                while i < num + 1:
                    dp[i] = dp[i - 1] + math.log10(i)
                    i += 1
                highest_calculated = i
            print(int(dp[num]))
    except EOFError:
        pass


if __name__ == '__main__':
    main()

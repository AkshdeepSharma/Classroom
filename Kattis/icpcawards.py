def main():
    N = int(input())
    ans = []
    uni_dict = {}
    for _ in range(N):
        uni, team = input().split()
        if uni not in uni_dict:
            uni_dict[uni] = 1
            if len(ans) < 12:
                ans.append([uni, team])
    for i in range(len(ans)):
        print(" ".join(ans[i]))


if __name__ == '__main__':
    main()

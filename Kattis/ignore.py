def main():
    memo = []
    try:
        while True:
            K = int(input())
            if K <= len(memo):
                print(memo[K - 1])
                continue
            curr_K = len(memo)
            curr_num = 0
            if memo:
                curr_num = flipNums(list(str(memo[-1])))
            while curr_K < K:
                curr_num = str(int(curr_num) + 1)
                num_set = set(list(curr_num))
                if '3' in num_set or '4' in num_set or '7' in num_set:
                    continue
                curr_K += 1
                memo.append(flipNums(list(curr_num)))
            print(memo[-1])
    except EOFError:
        pass


def flipNums(num):
    for i, char in enumerate(num):
        if char == '6':
            num[i] = '9'
        elif char == '9':
            num[i] = '6'
    return "".join(num)[::-1]


if __name__ == "__main__":
    main()

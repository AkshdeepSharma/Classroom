def main():
    cases = int(input())
    for _ in range(cases):
        people, issues = map(int, input().split())
        matrix = []
        for _ in range(people):
            matrix.append(list(input()))
        print(getMajorityOpinion(matrix, people, issues))


def getMajorityOpinion(matrix, people, issues):
    ans = []
    for i in range(issues):
        zeroCount = oneCount = 0
        for j in range(people):
            if matrix[j][i] == '0':
                zeroCount += 1
            else:
                oneCount += 1
        if zeroCount >= oneCount:
            ans.append('0')
        else:
            ans.append('1')
    return "".join(ans)


if __name__ == "__main__":
    main()

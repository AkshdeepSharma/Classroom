N = int(input())

for i in range(N):
    answer = ''
    a = input()
    b = input()
    for j in range(len(a)):
        if a[j] == b[j]:
            answer += '.'
        else:
            answer += '*'
    print(a)
    print(b)
    print(answer)


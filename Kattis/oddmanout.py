N = int(input())
case = 0
for i in range(N):
    case += 1
    b = int(input())
    guestNums = input().split(' ')
    guestNums = [int(x) for x in guestNums]
    for j in range(len(guestNums)):
        if guestNums.count(guestNums[j]) == 1:
            print('Case #' + str(case) + ":", str(guestNums[j]))

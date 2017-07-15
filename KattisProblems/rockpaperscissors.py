while True:
    win1, win2, loss1, loss2 = 0, 0, 0, 0
    nAndK = input().split(' ')
    if nAndK == 0:
        break
    n = int(nAndK[0])
    k = int(nAndK[1])
    for i in range((k * n * (n - 1)) // 2):

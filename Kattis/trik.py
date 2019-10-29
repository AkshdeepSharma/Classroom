moves = input()
ball = 1

for i in moves:
    if i == 'A' and ball == 1:
        ball = 2
    elif i == 'A' and ball == 2:
        ball = 1
    elif i == 'B' and ball == 2:
        ball = 3
    elif i == 'B' and ball == 3:
        ball = 2
    elif i == 'C' and ball == 1:
        ball = 3
    elif i == 'C' and ball == 3:
        ball = 1

print(ball)

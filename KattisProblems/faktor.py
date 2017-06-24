aAndI = input().split(' ')
A = int(aAndI[0])
I = int(aAndI[1])
scientists = A * I

while scientists / A > (I - 1):
    scientists -= 1

print(scientists + 1)

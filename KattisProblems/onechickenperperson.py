nAndM = input().split(' ')
n = int(nAndM[0])
m = int(nAndM[1])

if n > m:
    if n - m != 1:
        print('Dr. Chaz needs', n - m, 'more pieces of chicken!')
    else:
        print('Dr. Chaz needs', n - m, 'more piece of chicken!')
elif m > n:
    if m - n != 1:
        print('Dr. Chaz will have', m - n, 'pieces of chicken left over!')
    else:
        print('Dr. Chaz will have', m - n, 'piece of chicken left over!')
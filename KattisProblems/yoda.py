num1 = list(input())
num2 = list(input())

num1 = num1[::-1]
num2 = num2[::-1]

if len(num1) > len(num2):
    num3 = num2
    num4 = num1
else:
    num3 = num1
    num4 = num2

for i in range(len(num3)):
    if num3[i] > num4[i]:
        num4[i] = '-'
    elif num3[i] < num4[i]:
        num3[i] = '-'


def clean(num):
    count = num.count('-')
    for j in range(count):
        num.remove('-')


def zero(num):
    for p in range(len(num)):
        if num[p] == 0 and len(num) > 0:
            del num[i]
        else:
            break

clean(num3)
clean(num4)
num3 = num3[::-1]
num4 = num4[::-1]
num3 = ''.join(num3)
num4 = ''.join(num4)
zero(num3)
zero(num4)

if len(num1) > len(num2):
    print(num4)
    if len(num3) == 0:
        print('YODA')
    else:
        print(num3)
elif len(num2) < len(num1):
    if len(num3) == 0:
        print('YODA')
    else:
        print(num3)
    print(num4)
else:
    if len(num3) == 0:
        print('YODA')
    else:
        print(num3)
    if len(num4) == 0:
        print('YODA')
    else:
        print(num4)


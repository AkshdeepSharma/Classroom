num1 = input()[::-1]
num2 = input()[::-1]
answer1 = []
answer2 = []
count1 = len(num1)
count2 = len(num2)
if len(num1) >= len(num2):
    for i in range(len(num2)):
        if num2[i] > num1[i]:
            answer2.insert(0, num2[i])
        elif num2[i] < num1[i]:
            answer1.insert(0, num1[i])
        else:
            answer2.insert(0, num2[i])
            answer1.insert(0, num1[i])
elif len(num1) < len(num2):
    for i in range(len(num1)):
        if num1[i] > num2[i]:
            answer2.insert(0, num1[i])
        elif num1[i] < num2[i]:
            answer1.insert(0, num2[i])
        else:
            answer2.insert(0, num1[i])
            answer1.insert(0, num2[i])
if len(num1) > len(num2):
    for i in range(count2, count1):
        answer1.insert(0, num1[i])
elif len(num1) < len(num2):
    for i in range(count1, count2):
        answer1.insert(0, num2[i])
answer1 = [int(x) for x in answer1]
answer2 = [int(x) for x in answer2]

if len(answer1) == 0:
    answer1.append('YODA')
elif sum(answer1) == 0:
    answer1 = ['0']
if len(answer2) == 0:
    answer2.append('YODA')
elif sum(answer2) == 0:
    answer2 = ['0']
answer1 = [str(x) for x in answer1]
answer2 = [str(x) for x in answer2]
if len(num2) > len(num1):
    print(''.join(answer2))
    print(''.join(answer1))
else:
    print(''.join(answer1))
    print(''.join(answer2))

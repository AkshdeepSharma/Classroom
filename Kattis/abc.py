numbers = input().split(' ')
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
letters = input()
answer = ''
numbers = sorted(numbers)

for i in letters:
    if i == 'A':
        answer += str(numbers[0]) + ' '
    elif i == 'B':
        answer += str(numbers[1]) + ' '
    elif i == 'C':
        answer += str(numbers[2]) + ' '

answer = answer[:-1]
print(answer)

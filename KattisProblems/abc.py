numbers = input().split(' ')
letters = input()

numbers = sorted(numbers)
print (numbers)

answer = ''
for i in letters:
    if i == 'A':
        answer += numbers[0] + ' '
    elif i == 'B':
        answer += numbers[1] + ' '
    elif i == 'C':
        answer += numbers[2] + ' '

print(answer)

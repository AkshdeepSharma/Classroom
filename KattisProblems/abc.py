numbers = input().split(' ')
letters = input()
answer = ''
numbers2 = sorted(numbers)

for i in letters:
    if i == 'A':
        answer += numbers2[0] + ' '
    elif i == 'B':
        answer += numbers2[1] + ' '
    elif i == 'C':
        answer += numbers2[2] + ' '

print(answer)

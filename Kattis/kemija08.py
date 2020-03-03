kemija = list(input())
answer = ''
i = 0

while i < len(kemija):
    if kemija[i] in 'aeiou':
        answer += kemija[i]
        i += 3
    else:
        answer += kemija[i]
        i += 1
print(answer)

sequence = input()
countU = sequence.count('U')
countD = sequence.count('D')
upDown = 0


def up(toilets):
    if toilets.startswith('U'):
        answer = (countD * 2)
    else:
        if sequence[1] == 'D':
            answer = (countD - 1) * 2 - 1
        else:
            answer = (countD * 2 - 1)
    return answer


def down(toilets):
    if toilets.startswith('D'):
        answer = (countU * 2)
    else:
        if sequence[1] == 'U':
            answer = (countU - 1) * 2 - 1
        else:
            answer = (countU * 2 - 1)
    return answer

print(up(sequence))
print(down(sequence))
for i in range(len(sequence) - 1):
    if sequence[i] != sequence[i + 1]:
        upDown += 1
print(upDown)

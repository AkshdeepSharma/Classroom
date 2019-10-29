name = list(input())
name.append(' ')
newName = []
answer = ''
for i in range(len(name) - 1):
    if name[i] != name[i + 1]:
        newName.append(name[i])

for i in range(len(newName)):
    answer += str(newName[i])

print(answer)

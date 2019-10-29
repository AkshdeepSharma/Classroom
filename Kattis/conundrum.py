cipherText = input()
count = 0
per = ''

for i in range(len(cipherText) // 3):
    per += 'PER'

for j in range(len(cipherText)):
    if cipherText[j] != per[j]:
        count += 1

print(count)

word = input().split('-')
shortVariation = ''
for i in range(len(word)):
    shortVariation += word[i][0]
print(shortVariation)

s = 'abcbcd'
s = s + '.'

maxWord = ''
testWord = ''

for i in range(len(s) - 1):
    
    if s[i] <= s[i + 1]:
        testWord += s[i]
        
    elif s[i] > s[i + 1]:
        testWord += s[i]
        
        if len(testWord) > len(maxWord):
            maxWord = testWord
            testWord = ''
        else:
            testWord = ''

print (maxWord)
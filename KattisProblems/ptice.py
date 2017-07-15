N = int(input())
question = input()
scoreAdrian, scoreBruno, scoreGoran = 0, 0, 0
guessAdrian, guessBruno, guessGoran = '', '', ''

for i in range(len(question) // 2):
    guessAdrian += "ABC"
for j in range(len(question) // 2):
    guessBruno += "BABC"
for k in range(len(question) // 2):
    guessGoran += "CCAABB"

for l in range(len(question)):
    if question[l] == guessAdrian[l]:
        scoreAdrian += 1
    if question[l] == guessBruno[l]:
        scoreBruno += 1
    if question[l] == guessGoran[l]:
        scoreGoran += 1

num = max(scoreAdrian, scoreBruno, scoreGoran)
print(num)
if num == scoreAdrian:
    print('Adrian')
if num == scoreBruno:
    print('Bruno')
if num == scoreGoran:
    print('Goran')

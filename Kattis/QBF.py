num = int(input())
alphabet = list('abcdefghijklmnopqrstuvwxyz')
check = list()

for i in range(num):
    check = alphabet[:]
    phrase = input()
    phrase = phrase.lower()
    phrase = ''.join(char for char in phrase if char in check)
    phrase.splitlines()
    for j in phrase:
        if j in check:
            check.remove(j)
    if len(check) == 0:
        print('pangram')
    else:
        print('missing', str(''.join(check)))

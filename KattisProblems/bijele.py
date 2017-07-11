pieces = input().split(' ')
pieces = [int(x) for x in pieces]
validPieces = [1, 1, 2, 2, 2, 8]
actualPieces = ''

for i in range(len(validPieces)):
    actualPieces += str((validPieces[i] - pieces[i]))
    actualPieces += ' '

print(actualPieces)

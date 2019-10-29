cards = input()

T = cards.count('T')
C = cards.count('C')
G = cards.count('G')
seven = min(T, C, G)

score = T ** 2 + C ** 2 + G ** 2 + seven * 7
print(score)

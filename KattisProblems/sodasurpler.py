efc = input().split(' ')
e, f, c = int(efc[0]), int(efc[1]), int(efc[2])

bottlesOwned = e + f
bottlesBought = 0
while bottlesOwned > c:
    bottlesBought += (e + f) // c
    bottlesOwned -= (e + f) // c + bottlesBought

print(bottlesBought)

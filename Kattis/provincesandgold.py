def getVictoryCard(buying_power):
    if buying_power >= 8:
        victory_card = 'Province'
    elif buying_power >= 5:
        victory_card = 'Duchy'
    elif buying_power >= 2:
        victory_card = 'Estate'
    else:
        victory_card = None
    return victory_card


def getTreasureCard(buying_power):
    if buying_power >= 6:
        treasure_card = 'Gold'
    elif buying_power >= 3:
        treasure_card = 'Silver'
    else:
        treasure_card = 'Copper'
    return treasure_card


def main():
    G, S, C = map(int, input().split())
    buying_power = 3 * G + 2 * S + C
    victory_card = getVictoryCard(buying_power)
    treasure_card = getTreasureCard(buying_power)
    if not victory_card:
        print(treasure_card)
    else:
        print(victory_card + " or " + treasure_card)


if __name__ == '__main__':
    main()

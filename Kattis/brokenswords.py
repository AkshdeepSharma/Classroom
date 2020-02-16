def getNumSwords(sword_pieces):
    makeable_swords = min(sword_pieces['TB'] // 2, sword_pieces['LR'] // 2)
    remaining_TB_slats = sword_pieces['TB'] - (makeable_swords * 2)
    remaining_LR_slats = sword_pieces['LR'] - (makeable_swords * 2)
    return [makeable_swords, remaining_TB_slats, remaining_LR_slats]


def main():
    sword_pieces = {'TB': 0, 'LR': 0}
    num_broken_swords = int(input())
    for _ in range(num_broken_swords):
        slats = input()
        sword_pieces['TB'] += 2 - (int(slats[0]) + int(slats[1]))
        sword_pieces['LR'] += 2 - (int(slats[2]) + int(slats[3]))
    ans = getNumSwords(sword_pieces)
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

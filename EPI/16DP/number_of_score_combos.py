# 16.1 in EPI NOTE: THIS IS NOT THE FINAL SOLUTION


def score_combos(score):
    if score == 2 or score == 3 or score == 7:
        return 1
    elif score < 2:
        return 0
    else:
        return score_combos(score - 2) + score_combos(score - 3) + score_combos(score - 7)


print(score_combos(12))

print([[1] + [0] * 12 for _ in range(3)])
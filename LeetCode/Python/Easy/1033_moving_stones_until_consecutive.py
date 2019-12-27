class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        stones = sorted([a,b,c])
        if (abs(b - a) == 2 and abs(c - a) != 1) or (abs(c - a) == 2 and abs(b - a) != 1) or (abs(b - c) == 2 and abs(b - a) != 1):
            ans = 1
        elif stones[1] + 1 == stones[2] and stones[0] + 1 == stones[1]:
            ans = 0
        elif stones[1] + 1 == stones[2] or stones[0] + 1 == stones[1]:
            ans = 1
        else:
            ans = 2
        return [ans, (stones[2] - stones[1] - 1) + (stones[1] - stones[0] - 1)]
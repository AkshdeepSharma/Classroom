class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        for i in range(n // 2 * - 1, n // 2 + 1):
            if i == 0:
                continue
            res.append(i)
        return res if n % 2 == 0 else res + [0]

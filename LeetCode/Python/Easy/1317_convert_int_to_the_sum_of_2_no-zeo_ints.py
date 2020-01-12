class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for a in range(n, 0, -1):
            b = n - a
            if '0' not in set(str(a)) and '0' not in set(str(b)):
                return [a, b]

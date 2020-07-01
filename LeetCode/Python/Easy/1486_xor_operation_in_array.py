class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        l = [start + 2 * i for i in range(n)]
        return reduce(lambda x, y: x ^ y, l)

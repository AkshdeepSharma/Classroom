class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                factors.append(i)
            if len(factors) == k:
                return i
        if len(factors) == k - 1:
            return n
        return -1

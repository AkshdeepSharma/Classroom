class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        for i in range(1, n // 7 + 1):
            total += sum(range(i, i + 7))
        return total + sum(range(n // 7 + 1, n // 7 + 1 + n % 7))

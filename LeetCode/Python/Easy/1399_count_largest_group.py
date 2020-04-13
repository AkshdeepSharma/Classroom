class Solution:
    def sumDigits(self, n):
        r = 0
        while n:
            r, n = r + n % 10, n // 10
        return r

    def countLargestGroup(self, n: int) -> int:
        counts = [0] * (n + 1)
        best = 0
        best_count = 0
        for num in range(1, n + 1):
            counts[self.sumDigits(num)] += 1
        for i in range(len(counts)):
            if counts[i] > best:
                best = counts[i]
                best_count = 1
            elif counts[i] == best:
                best_count += 1
        return best_count

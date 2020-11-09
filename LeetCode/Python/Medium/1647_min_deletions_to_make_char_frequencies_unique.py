class Solution:
    def minDeletions(self, s: str) -> int:
        count = {}
        seen_counts = set()
        ans = 0
        for c in s:
            if c not in count:
                count[c] = 0
            count[c] += 1
        for val in count.values():
            while val in seen_counts:
                val -= 1
                ans += 1
            if val > 0:
                seen_counts.add(val)
        return ans

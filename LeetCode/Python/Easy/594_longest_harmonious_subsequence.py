class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = {}
        curr, best = 0, 0
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        for key, val in count.items():
            curr = val
            if key + 1 in count:
                best = max(curr + count[key + 1], best)
            if key - 1 in count:
                best = max(curr + count[key - 1], best)
        return best

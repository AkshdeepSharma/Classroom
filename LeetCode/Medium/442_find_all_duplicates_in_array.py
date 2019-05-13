class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = {}
        res = []
        for c in nums:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        for key, val in d.items():
            if val == 2:
                res.append(key)
        return res
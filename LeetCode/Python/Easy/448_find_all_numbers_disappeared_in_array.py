class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        d = {}
        res = []
        for num in nums:
            if num not in d:
                d[num] = 1
        for i in range(1, len(nums) + 1):
            if i not in d:
                res.append(i)
        return res
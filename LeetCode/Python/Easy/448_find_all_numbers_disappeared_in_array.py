class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                continue
            nums[abs(num) - 1] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res

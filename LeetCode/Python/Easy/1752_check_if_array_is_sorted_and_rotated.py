class Solution:
    def check(self, nums: List[int]) -> bool:
        rotated = False
        for i in range(1, len(nums)):
            if not rotated and nums[i - 1] > nums[i]:
                rotated = True
            elif rotated and nums[i - 1] > nums[i]:
                return False
        return (rotated and nums[0] >= nums[-1]) or not rotated

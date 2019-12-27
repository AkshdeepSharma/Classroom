class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1] * len(nums)
        product = 1
        for i in range(len(nums)):
            output[i] *= product
            product *= nums[i]
        product = 1
        for j in reversed(range(len(nums))):
            output[j] *= product
            product *= nums[j]
        return output
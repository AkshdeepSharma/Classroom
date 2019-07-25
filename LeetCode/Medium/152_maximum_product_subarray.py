class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = mindp = maxdp = nums[0]
        
        for num in nums[1:]:
            maxdp, mindp = max(num, num * maxdp, num * mindp), min(num, num * maxdp, num * mindp)
            max_num = max(max_num, maxdp)
        return max_num
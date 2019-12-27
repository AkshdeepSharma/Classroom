class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        value_of_nums = [0] * 10001
        for num in nums:
            value_of_nums[num] += num
        return self.get_points(value_of_nums)

    def get_points(self, nums):
        prev, curr = 0, 0
        for num in nums:
            prev, curr = curr, max(prev + num, curr)
        return curr

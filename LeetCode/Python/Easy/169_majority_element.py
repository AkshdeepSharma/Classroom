class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority = {}
        for num in nums:
            if num in majority:
                majority[num] += 1
            else:
                majority[num] = 1
        return max(majority, key=majority.get)
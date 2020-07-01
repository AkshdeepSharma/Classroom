class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def getFirstAndSecondLargestNum(nums):
            first = second = float('-inf')
            for num in nums:
                if num > first:
                    first, second = num, first
                elif first >= num > second:
                    second = num
            return [first, second]
        a, b = getFirstAndSecondLargestNum(nums)
        return (a - 1) * (b - 1)

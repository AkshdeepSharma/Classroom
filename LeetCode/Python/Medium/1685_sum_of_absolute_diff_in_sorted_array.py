class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        result = []
        left_sum, right_sum = 0, sum(nums)
        for i in range(len(nums)):
            right_sum -= nums[i]
            result.append(abs(right_sum - (len(nums) - i - 1) *
                              nums[i]) + abs(left_sum - (i * nums[i])))
            left_sum += nums[i]
        return result

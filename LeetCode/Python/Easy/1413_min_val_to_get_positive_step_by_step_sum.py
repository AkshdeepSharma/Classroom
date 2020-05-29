class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minimumSum = 0
        currSum = 0
        for num in nums:
            currSum += num
            minimumSum = min(minimumSum, currSum)
        return (minimumSum - 1) * -1 if minimumSum <= 0 else 1

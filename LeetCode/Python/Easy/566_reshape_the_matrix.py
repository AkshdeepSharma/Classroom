from functools import reduce


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        ans = []
        if r * c != len(nums) * len(nums[0]):
            return nums
        flat_nums = reduce(lambda x, y: x + y, nums)
        for i in range(0, len(flat_nums), c):
            ans.append(flat_nums[i:i + c])
        return ans

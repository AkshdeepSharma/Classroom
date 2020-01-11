class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums) * len(nums[0]) != r * c:
            return nums
        res = []
        temp = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                temp.append(nums[i][j])
                if len(temp) == c:
                    res.append(temp)
                    temp = []
        return res

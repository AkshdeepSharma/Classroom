from itertools import combinations


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # kek
        return sum([list(map(list, combinations(nums, i))) for i in range(len(nums) + 1)], [])

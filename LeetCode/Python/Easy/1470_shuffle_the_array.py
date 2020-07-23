class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(len(nums) // 2):
            ans += [nums[i], nums[i + n]]
        return ans

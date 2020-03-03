class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 102
        ans = []
        for num in nums:
            count[num + 1] += 1
        for i in range(1, 102):
            count[i] += count[i - 1]
        for num in nums:
            ans.append(count[num])
        return ans
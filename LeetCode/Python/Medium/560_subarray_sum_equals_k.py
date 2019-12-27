from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        running_sum = 0
        d = defaultdict(int)
        res = 0
        for num in nums:
            running_sum += num
            sum = running_sum - k
            if sum in d:
                res += d[sum]
            if running_sum == k:
                res += 1
            d[running_sum] += 1
        return res
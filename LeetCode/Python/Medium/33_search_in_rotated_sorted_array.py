class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        pivot = lo
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            pivoted_mid = (mid + pivot) % len(nums)
            if nums[pivoted_mid] == target:
                return pivoted_mid
            elif nums[pivoted_mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1

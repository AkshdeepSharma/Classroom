class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower, upper = 0, len(nums) - 1
        while lower <= upper:
            mid = (lower + upper) // 2
            if nums[mid] > target:
                upper = mid - 1
            elif nums[mid] < target:
                lower = mid + 1
            else:
                return mid
        return -1

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest_sequence = 1
        if not nums:
            return 0
        for num in nums:
            current_longest = 1
            if num + 1 in nums:
                curr_num = num + 1
                while curr_num in nums:
                    current_longest += 1
                    curr_num += 1
                longest_sequence = max(longest_sequence, current_longest)
        return longest_sequence
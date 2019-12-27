class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:
            mid = len(nums) // 2
            L = nums[:mid]
            R = nums[mid:]
            self.sortArray(L)
            self.sortArray(R)

            i = j = k = 0
            while len(L) > i and len(R) > j:
                if L[i] < R[j]:
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1
                k += 1

            while len(L) > i:
                nums[k] = L[i]
                i += 1
                k += 1
            while len(R) > j:
                nums[k] = R[j]
                j += 1
                k += 1
        return nums
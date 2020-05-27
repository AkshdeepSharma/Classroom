class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        oneIndexes = []
        for i in range(len(nums)):
            if nums[i] == 1:
                if not oneIndexes:
                    oneIndexes.append(i)
                    continue
                if i - oneIndexes[-1] <= k:
                    return False
                oneIndexes.append(i)
        return True

class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        diff = (sum(A) - sum(B)) // 2
        A = set(A)
        for num in B:
            if num + diff in A:
                return [num + diff, num]

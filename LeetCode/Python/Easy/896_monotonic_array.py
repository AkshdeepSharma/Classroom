class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        inc = dec = False
        for i in range(1, len(A)):
            if A[i - 1] > A[i]:
                dec = True
            elif A[i - 1] < A[i]:
                inc = True
            if inc and dec:
                return False
        return True

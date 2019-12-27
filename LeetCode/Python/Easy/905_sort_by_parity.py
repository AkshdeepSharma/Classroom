class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        front, back = 0, len(A) - 1
        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[i], A[front] = A[front], A[i]
                front += 1
        for j in range(len(A)):
            if A[j] % 2 == 1:
                A[i], A[back] = A[back], A[i]
                back -= 1
        return A

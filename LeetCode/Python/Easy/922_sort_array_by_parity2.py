class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        ans = [0] * len(A)
        even, odd = 0, 1
        for num in A:
            if num % 2 == 0:
                ans[even] = num
                even += 2
            else:
                ans[odd] = num
                odd += 2
        return ans

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            divisors = {1, num}
            for j in range(2, math.floor(sqrt(num)) + 1):
                if num % j == 0:
                    divisors.add(j)
                    divisors.add(num // j)
                    if len(divisors) > 4:
                        break
            if len(divisors) == 4:
                res += sum(divisors)
        return res

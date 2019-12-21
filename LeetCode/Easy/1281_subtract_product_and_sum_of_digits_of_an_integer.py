class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = list(map(int, str(n)))
        n_product = 1
        for x in n:
            n_product *= x
        return n_product - sum(n)

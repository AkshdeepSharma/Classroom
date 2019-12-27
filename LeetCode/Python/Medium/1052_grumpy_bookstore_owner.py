class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        max_sum, curr_satisfied, max_satisfied = 0, 0, 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                max_sum += customers[i]
                customers[i] = 0
        for i in range(len(customers)):
            curr_satisfied += customers[i]
            if i >= X:
                curr_satisfied -= customers[i - X]
            max_satisfied = max(max_satisfied, curr_satisfied)
        return max_sum + max_satisfied
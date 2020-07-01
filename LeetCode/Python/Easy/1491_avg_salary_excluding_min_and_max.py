class Solution:
    def average(self, salary: List[int]) -> float:
        min_sal, max_sal = min(salary), max(salary)
        return (sum(salary) - max_sal - min_sal) / (len(salary) - 2)

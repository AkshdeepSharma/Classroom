class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        n = len(costs) / 2
        res = 0
        for i in range(len(costs)):
            n -= 1
            if n >= 0:
                res += costs[i][0]
            else:
                res += costs[i][1]
        return res
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], workers: List[int]) -> int:
        max_profit = i = best = 0
        sorted_profit = sorted(zip(profit, difficulty), key=lambda x: x[1])
        for worker in sorted(workers):
            while i < len(sorted_profit) and worker >= sorted_profit[i][1]:
                best = max(best, sorted_profit[i][0])
                i += 1
            max_profit += best
        return max_profit

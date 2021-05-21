class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        pop = [0] * 2051
        ans = 0
        for year in logs:
            pop[year[0]] += 1
            pop[year[1]] -= 1
        for i in range(1950, 2051):
            pop[i] += pop[i - 1]
            if pop[i] > pop[ans]:
                ans = i
        return ans
                
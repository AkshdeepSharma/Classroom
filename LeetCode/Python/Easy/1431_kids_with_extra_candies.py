class Solution:
    def kidsWithCandies(self, candies: List[int], extra: int) -> List[bool]:
        max_candies = max(candies)
        for i in range(len(candies)):
            if candies[i] + extra >= max_candies:
                candies[i] = True
            else:
                candies[i] = False
        return candies

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(1, len(points)):
            x = abs(points[i][0] - points[i-1][0])
            y = abs(points[i][1] - points[i-1][1])
            time += max(x, y)
        return time

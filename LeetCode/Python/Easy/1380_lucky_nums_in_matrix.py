class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        rotated = [list(reversed(col)) for col in zip(*matrix)]
        for i in range(len(matrix)):
            mini = min(matrix[i])
            index = matrix[i].index(mini)
            if mini == max(rotated[index]):
                ans.append(mini)
        return ans

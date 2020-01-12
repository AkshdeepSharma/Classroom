class Solution:
    def getRow(self, k: int) -> List[int]:
        if k == 0:
            return [1]
        row = [1, 1]
        for _ in range(k - 1):
            row = [1] + [row[i] + row[i - 1] for i in range(1, len(row))] + [1]
        return row

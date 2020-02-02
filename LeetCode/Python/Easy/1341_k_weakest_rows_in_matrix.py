class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = []
        ans = []
        for i in range(len(mat)):
            rows.append((i, sum(mat[i])))
        rows.sort(key=lambda x: x[1])
        for i in range(k):
            ans.append(rows[i][0])
        return ans

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = []
        for i, val in enumerate(arr):
            temp.append((val, i))
        temp = sorted(temp, key=lambda x: x[0])
        rank, curr = 0, float('-inf')
        for i in range(len(temp)):
            if temp[i][0] > curr:
                curr = temp[i][0]
                rank += 1
            arr[temp[i][1]] = rank
        return arr
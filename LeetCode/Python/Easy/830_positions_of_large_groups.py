class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        ans = []
        continuous_count = 1
        for i in range(1, len(S)):
            if S[i] == S[i - 1]:
                continuous_count += 1
            else:
                if continuous_count > 2:
                    ans.append([i - continuous_count, i - 1])
                continuous_count = 1
        if continuous_count > 2:
            ans.append([i - continuous_count + 1, i])
        return ans

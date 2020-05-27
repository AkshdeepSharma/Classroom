class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        targetSet = set(target)
        for i in range(1, target[-1] + 1):
            ans.append("Push")
            if i not in targetSet:
                ans.append("Pop")
        return ans

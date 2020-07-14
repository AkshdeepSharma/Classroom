class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        ans = []
        for i, num in enumerate(groupSizes):
            if num not in groups:
                groups[num] = []
            groups[num].append(i)
        for key, val in groups.items():
            for i in range(0, len(val), key):
                ans.append(val[i:i + key])
        return ans

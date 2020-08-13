class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        best = float('inf')
        d = {}
        for i in range(len(list1)):
            d[list1[i]] = i
        for i in range(len(list2)):
            if list2[i] in d:
                if i + d[list2[i]] < best:
                    best = i + d[list2[i]]
                    ans = [list2[i]]
                elif i + d[list2[i]] == best:
                    ans.append(list2[i])
        return ans
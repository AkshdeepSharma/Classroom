class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        l = r = 0
        res = [0]
        for c in S:
            if c == 'I':
                r += 1
                res.append(r)
            else:
                l -= 1
                res.append(l)
        return [i - l for i in res]
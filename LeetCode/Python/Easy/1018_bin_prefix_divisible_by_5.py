class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        binary = ''
        res = []
        for num in A:
            binary += str(num)
            if int(binary, 2) % 5 == 0:
                res.append(True)
            else:
                res.append(False)
        return res
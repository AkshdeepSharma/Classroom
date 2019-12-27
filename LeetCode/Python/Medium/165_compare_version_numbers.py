class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))
        while len(v1) != len(v2):
            if len(v1) > len(v2):
                v2.append(0)
            else:
                v1.append(0)
        for i in range(len(v1)):
            if v1[i] - v2[i] < 0:
                return -1
            elif v1[i] - v2[i] > 0:
                return 1
        return 0

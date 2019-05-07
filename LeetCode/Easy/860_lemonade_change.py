class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        numFives = 0
        numTens = 0
        for num in bills:
            if num == 5:
                numFives += 1
            elif num == 10:
                if numFives >= 1:
                    numFives -= 1
                    numTens += 1
                else:
                    return False
            elif num == 20:
                if numFives >= 1 and numTens >= 1:
                    numFives -= 1
                    numTens -= 1
                elif numFives >= 3:
                    numFives -= 3
                else:
                    return False
        return True
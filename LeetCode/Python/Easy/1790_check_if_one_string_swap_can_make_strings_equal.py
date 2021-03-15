class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        missing_letters1, missing_letters2 = set(), set()
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
                if count > 2:
                    return False
                missing_letters1.add(s1[i])
                missing_letters2.add(s2[i])
        return True if missing_letters1 == missing_letters2 else False

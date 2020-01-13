class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = {}
        for c in magazine:
            if c in mag:
                mag[c] += 1
            else:
                mag[c] = 1
        for c in ransomNote:
            if c in mag:
                mag[c] -= 1
                if mag[c] < 0:
                    return False
            else:
                return False
        return True

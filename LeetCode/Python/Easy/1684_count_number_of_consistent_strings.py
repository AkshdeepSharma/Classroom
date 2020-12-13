class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        allowed = set(list(allowed))
        for word in words:
            count += 1
            for c in word:
                if c not in allowed:
                    count -= 1
                    break
        return count

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxV = currV = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for i, c in enumerate(s):
            if c in vowels:
                currV += 1
            if i >= k and s[i - k] in vowels:
                currV -= 1
            maxV = max(maxV, currV)
        return maxV

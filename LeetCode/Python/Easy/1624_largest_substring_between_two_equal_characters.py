class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        character_indexes = {}
        max_length = -1
        for i, c in enumerate(s):
            if c not in character_indexes:
                character_indexes[c] = []
            character_indexes[c].append(i)
        for val in character_indexes.values():
            if len(val) > 1:
                max_length = max(max_length, val[-1] - val[0] - 1)
        return max_length

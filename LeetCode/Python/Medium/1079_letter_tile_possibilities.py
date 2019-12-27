from itertools import permutations


class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        hashset = set()

        def dfs(permutation, tiles):
            if permutation in hashset:
                return
            if permutation not in hashset or not tiles:
                hashset.add(permutation)
            for i in range(len(tiles)):
                dfs(permutation + tiles[i], tiles[:i] + tiles[i + 1:])
        dfs('', tiles)
        return len(hashset) - 1

    def numTilePossibilitiesUsingPermutation(self, tiles):
        l = []
        for j in range(1, len(tiles) + 1):
            l.extend(list(permutations(list(tiles), j)))
        return len(set(l))

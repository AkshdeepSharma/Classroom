class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        d = collections.deque()
        for i in reversed(sorted(deck)):
            d.rotate()
            d.appendleft(i)
        return list(d)
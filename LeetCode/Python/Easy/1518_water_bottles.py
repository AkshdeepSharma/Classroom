class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink = numBottles
        while numBottles >= numExchange:
            leftover = numBottles % numExchange
            numBottles //= numExchange
            drink += numBottles
            numBottles += leftover
        return drink

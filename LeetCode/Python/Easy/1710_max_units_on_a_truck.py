class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        units = 0
        boxTypes = sorted(boxTypes, key=lambda x: -x[1])
        for boxes in boxTypes:
            if boxes[0] <= truckSize:
                units += boxes[0] * boxes[1]
                truckSize -= boxes[0]
            else:
                units += truckSize * boxes[1]
                break
        return units

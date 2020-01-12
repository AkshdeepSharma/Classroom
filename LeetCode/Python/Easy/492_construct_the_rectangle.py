class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        if area == 0:
            return [0, 0]
        width = int(math.sqrt(area))
        while area % width != 0:
            width -= 1
        return [area//width, width]

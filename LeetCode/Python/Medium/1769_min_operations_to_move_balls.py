class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes_with_balls = []
        ans = []
        for i, box in enumerate(boxes):
            if box == '1':
                boxes_with_balls.append(i)
        for i in range(len(boxes)):
            operations = 0
            for box in boxes_with_balls:
                operations += abs(i - box)
            ans.append(operations)
        return ans

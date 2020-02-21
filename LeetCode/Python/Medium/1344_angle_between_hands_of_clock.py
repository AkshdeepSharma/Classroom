class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour = hour % 12 * 30 + minutes / 60 * 30
        minutes = minutes * 6
        angle = abs(hour - minutes)
        return angle if angle <= 180 else 360 - angle

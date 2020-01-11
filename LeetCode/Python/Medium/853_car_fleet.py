class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        last_time = -1
        fleets = 0
        times = [float(target - p) / s for p,
                 s in sorted(zip(position, speed))]
        for time in times[::-1]:
            if time > last_time:
                fleets += 1
                last_time = time
        return fleets

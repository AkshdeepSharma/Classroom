class Solution:
    def maxNumberOfFamilies(self, n: int, reserved_seats: List[List[int]]) -> int:
        num_families = 2 * n
        reserved_map = {}
        for seat in reserved_seats:
            if seat[0] not in reserved_map:
                reserved_map[seat[0]] = set()
            reserved_map[seat[0]].add(seat[1])
        for row in reserved_map:
            count = 0
            if 2 not in reserved_map[row] and 3 not in reserved_map[row] and 4 not in reserved_map[row] and 5 not in reserved_map[row]:
                count += 1
            if 6 not in reserved_map[row] and 7 not in reserved_map[row] and 8 not in reserved_map[row] and 9 not in reserved_map[row]:
                count += 1
            if 4 not in reserved_map[row] and 5 not in reserved_map[row] and 6 not in reserved_map[row] and 7 not in reserved_map[row] and count == 0:
                count += 1
            num_families += count - 2
        return num_families

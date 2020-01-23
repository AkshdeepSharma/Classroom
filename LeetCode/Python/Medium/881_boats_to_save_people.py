class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        i, j = 0, len(people) - 1
        num_boats = 0
        while i <= j:
            if i == j:
                i += 1
            elif people[i] + people[j] <= limit:
                i += 1
                j -= 1
            elif people[i] + people[j] > limit:
                j -= 1
            num_boats += 1
        return num_boats

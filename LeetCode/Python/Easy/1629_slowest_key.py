class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        best_char, longest_duration = keysPressed[0], releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            curr_duration = releaseTimes[i] - releaseTimes[i - 1]
            if curr_duration > longest_duration:
                best_char, longest_duration = keysPressed[i], curr_duration
            elif curr_duration == longest_duration:
                if ord(best_char) < ord(keysPressed[i]):
                    best_char, longest_duration = keysPressed[i], curr_duration
        return best_char

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = y = 0
        curr_direction = 0 # N=0, E=1, S=2, W=3
        for i in range(4):
            for c in instructions:
                if c == 'L':
                    curr_direction += 1
                elif c == 'R':
                    curr_direction += 3
                elif c == 'G':
                    if curr_direction == 0:
                        y += 1
                    elif curr_direction == 1:
                        x += 1
                    elif curr_direction == 2:
                        y -= 1
                    else:
                        x -= 1
                curr_direction %= 4
            if x == y == 0:
                return True
        return False
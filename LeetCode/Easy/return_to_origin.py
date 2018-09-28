class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        LR = UD = 0
        for move in moves:
            if move == 'L':
                LR -= 1
            elif move == 'R':
                LR += 1
            elif move == 'U':
                UD += 1
            elif move == 'D':
                UD -= 1
        return LR == UD == 0

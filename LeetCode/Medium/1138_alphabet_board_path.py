class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        res = ""
        i, j = 0, 0
        for k in range(len(target)):
            while True:
                if target[k] in board[i]:
                    if target[k] == board[i][j]:
                        res += ('!')
                        break
                    elif target[k] > board[i][j]:
                        j += 1
                        res += ("R")
                    elif target[k] < board[i][j]:
                        j -= 1
                        res += ("L")
                elif target[k] < board[i][0]:
                    i -= 1
                    res += "U"
                elif target[k] > board[i][-1]:
                    if i == 4 and target[k] == 'z':
                        for _ in range(j):
                            res += "L"
                        j = 0
                    i += 1
                    res += "D"
        return res
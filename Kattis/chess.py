blackTiles = {
    "A1": 1,
    "A3": 1,
    "A5": 1,
    "A7": 1,
    "B2": 1,
    "B4": 1,
    "B6": 1,
    "B8": 1,
    "C1": 1,
    "C3": 1,
    "C5": 1,
    "C7": 1,
    "D2": 1,
    "D4": 1,
    "D6": 1,
    "D8": 1,
    "E1": 1,
    "E3": 1,
    "E5": 1,
    "E7": 1,
    "F2": 1,
    "F4": 1,
    "F6": 1,
    "F8": 1,
    "G1": 1,
    "G3": 1,
    "G5": 1,
    "G7": 1,
    "H2": 1,
    "H4": 1,
    "H6": 1,
    "H8": 1,
}
whiteTiles = {
    "A2": 1,
    "A4": 1,
    "A6": 1,
    "A8": 1,
    "B1": 1,
    "B3": 1,
    "B5": 1,
    "B7": 1,
    "C2": 1,
    "C4": 1,
    "C6": 1,
    "C8": 1,
    "D1": 1,
    "D3": 1,
    "D5": 1,
    "D7": 1,
    "E2": 1,
    "E4": 1,
    "E6": 1,
    "E8": 1,
    "F1": 1,
    "F3": 1,
    "F5": 1,
    "F7": 1,
    "G2": 1,
    "G4": 1,
    "G6": 1,
    "G8": 1,
    "H1": 1,
    "H3": 1,
    "H5": 1,
    "H7": 1,
}

board = [
    ["A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8"],
    ["A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7"],
    ["A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6"],
    ["A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5"],
    ["A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4"],
    ["A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3"],
    ["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2"],
    ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1"]
]

num_testcases = int(input())


def findPath():
    positions = input()
    position1 = positions[0] + positions[2]
    position2 = positions[4] + positions[6]
    if (position1 in blackTiles and position2 in whiteTiles) or (position1 in whiteTiles and position2 in blackTiles):
        return("Impossible")
    else:
        if position1 == position2:
            return("0 " + position1[0] + " " + position1[1])
        else:
            row, col, row2, col2 = 8 - int(position1[1]), ord(position1[0]) - ord(
                "A"), 8 - int(position2[1]), ord(position2[0]) - ord("A")
            if abs(row2 - row) == abs(col2 - col):
                return("1 " + position1[0] + " " + position1[1] + " " + position2[0] + " " + position2[1])
            else:
                row3, col3 = row, col
                direction = 0
                while direction < 4:
                    if direction == 0:
                        row3 -= 1
                        col3 -= 1
                    elif direction == 1:
                        row3 += 1
                        col3 += 1
                    elif direction == 2:
                        row3 -= 1
                        col3 += 1
                    elif direction == 3:
                        row3 += 1
                        col3 -= 1
                    if row3 < 0 or row3 > 7 or col3 < 0 or col3 > 7:
                        row3, col3 = row, col
                        direction += 1
                    elif abs(row3 - row2) == abs(col3 - col2):
                        break

                position3 = board[row3][col3]
                return("2 " + position1[0] + " " + position1[1] + " " + position3[0] + " " + position3[1] + " " + position2[0] + " " + position2[1])


for i in range(num_testcases):
    print(findPath())

N = int(input())

while N != 0:
    pile1, pile2 = 0, 0
    for _ in range(N):
        command = input().split()
        action, num_plates = command[0], int(command[1])
        if action == "DROP":
            pile2 += num_plates
            print("DROP 2 " + str(num_plates))
        elif action == "TAKE":
            if pile1 >= num_plates:
                pile1 -= num_plates
                print("TAKE 1 " + str(num_plates))
            else:
                if pile1 != 0:
                    print("TAKE 1 " + str(pile1))
                    num_plates -= pile1
                    pile1 = 0
                print("MOVE 2->1 " + str(pile2))
                pile1 = pile2 - num_plates
                pile2 = 0
                print("TAKE 1 " + str(num_plates))
    print("")
    N = int(input())

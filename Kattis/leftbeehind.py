while True:
    inp1 = input().split(' ')
    if inp1 == ['0', '0']:
        break
    elif int(inp1[0]) + int(inp1[1]) == 13:
        print("Never speak again.")
    elif int(inp1[0]) == int(inp1[1]):
        print("Undecided.")
    elif int(inp1[0]) > int(inp1[1]):
        print("To the convention.")
    else:
        print("Left beehind.")

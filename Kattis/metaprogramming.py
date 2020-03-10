def main():
    variables = {}
    try:
        while True:
            ans = True
            command = list(input().split())
            if command[0] == 'define':
                variables[command[2]] = int(command[1])
            elif command[0] == 'eval':
                if command[1] not in variables or command[3] not in variables:
                    print('undefined')
                    continue
                if command[2] == '=':
                    ans = variables[command[1]] == variables[command[3]]
                if command[2] == '>':
                    ans = variables[command[1]] > variables[command[3]]
                if command[2] == '<':
                    ans = variables[command[1]] < variables[command[3]]
                if ans:
                    print("true")
                else:
                    print("false")
    except EOFError:
        pass


if __name__ == "__main__":
    main()

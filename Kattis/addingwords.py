try:
    translate = {}
    while True:
        command = input().split()
        if command[0] == "clear":
            translate = {}
        elif command[0] == "def":
            word, num = command[1], command[2]
            if word in translate:
                translate.pop(translate[word])
                translate.pop(word, None)
                translate.pop(num, None)
            translate[word] = num
            translate[num] = word
        else:
            expression = command[1:]
            successful_query = True
            for i in range(len(expression)):
                if expression[i] == "-" or expression[i] == "+" or expression[i] == "=":
                    continue
                elif expression[i] not in translate:
                    print(" ".join(command[1:]) + " unknown")
                    successful_query = False
                    break
                else:
                    expression[i] = translate[expression[i]]
            if successful_query:
                expression = " ".join(expression[:-1])
                num = eval(expression)
                if str(num) not in translate:
                    command.append("unknown")
                else:
                    command.append(translate[str(num)])
                print(" ".join(command[1:]))
except EOFError:
    pass

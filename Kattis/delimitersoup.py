def getUnmatchedBrace(parentheses_string):
    stack = []
    parentheses_dictionary = {"{": "}", "(": ")", "[": "]"}
    for i in range(len(parentheses_string)):
        if parentheses_string[i] in parentheses_dictionary:
            stack.append(parentheses_string[i])
        elif parentheses_string[i] == " ":
            continue
        else:
            if not stack or parentheses_dictionary[stack[-1]] != parentheses_string[i]:
                return parentheses_string[i] + " " + str(i)
            else:
                stack.pop()
    return "ok so far"


def main():
    length = int(input())
    parentheses_string = list(input())
    print(getUnmatchedBrace(parentheses_string))


if __name__ == "__main__":
    main()

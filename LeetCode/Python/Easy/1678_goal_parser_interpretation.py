class Solution:
    def interpret(self, command: str) -> str:
        interpreted_string = ""
        for i, c in enumerate(command):
            if c == 'G':
                interpreted_string += c
            elif c == ")":
                if command[i - 1] == "(":
                    interpreted_string += "o"
                else:
                    interpreted_string += "al"
        return interpreted_string
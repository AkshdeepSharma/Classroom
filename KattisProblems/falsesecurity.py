translate = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '_': '..--',
    ',': '.-.-',
    '.': '---.',
    '?': '----'
}

try:
    while True:
        code = []
        message = input()
        translatedMessage = ''
        decodedMessage = ''
        for i in message:
            translatedMessage += translate.get(i), ' '
            code.append(len(translate.get(i)))
        code = code[::-1]
        for i in range(len(code) - 1):
            decodedMessage += translatedMessage[list(translate.keys())[list(translate.values()).index(code[i])]]
        print(decodedMessage)
except EOFError:
    pass



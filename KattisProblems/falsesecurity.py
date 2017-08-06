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
}  # Creates dict for English to Morse Code
retranslate = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
    '..--': '_',
    '.-.-': ',',
    '---.': '.',
    '----': '?'
}  # Creates dict for Morse Code to English

try:  # Problem includes and EoF Error
    while True:
        # Define variables
        code = []
        message = input()
        morseCode, answer = '', ''
        count = -1
        # Translates English to Morse Code and appends length of each Morse letter to code
        for i in message:
            morseCode += translate.get(i)
            code.append(len(translate.get(i)))
        # Reverse code as part of encryption and convert string Morse code to list
        code = code[::-1]
        morseCode = list(morseCode)
        # Adds spaces (' ') in morseCode list in code order
        for i in range(len(code) - 1):
            count += code[i] + i - (i - 1)
            morseCode.insert(count, ' ')
        # Joins morseCode together and re-splits based on spaces. Example: ['.', ' ', '-', '-'] -> . -- -> ['.', '--']
        morseCode = ''.join(morseCode)
        morseCode = morseCode.split(' ')
        # Creates answer using the Morse Code to English dictionary
        for i in morseCode:
            answer += retranslate.get(i)
        print(answer)
except EOFError:
    pass

code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '0': '-----',

    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', 
    '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': ' '}

text = "Hello, my name is Ryan"

'''for ch in text:
    if(code.get(ch.upper())==None):
        print(code[' '], end=' ')
    else:
        print(code(ch.upper()), sep=" ", end=" ")'''

for ch in text:
    if code.get(ch.upper()) is None:   # use parentheses for .get()
        print(code[' '], end=' ')
    else:
        print(code[ch.upper()], end=' ')

for ch, morse in code.items():
    print(ch, morse)

for ch in text:
    if(code.get(ch.upper()))==None:
        print(code[' '], end=[' '])
    else:
        print(code[ch.upper()], end=' ', sep=' ')
# .upper will convert everything to upercase
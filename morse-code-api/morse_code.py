class MorseCode:
    ENG_TO_MORSE_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '1': '.----',
        '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.', '0': '-----',
        ':': '---...', ',': '--..--', '.': '.-.-.-',
        '?': '..--..', '-': '-....-', '(': '-.--.', ')': '-.--.-'
    }
    MORSE_TO_ENG_DICT = {val: key for key, val in ENG_TO_MORSE_DICT.items()}

    @staticmethod
    def encode(raw_text):
        output_text_buffer = []
        for ch in raw_text:
            if ch == ' ':
                output_text_buffer.append('/')
            else:
                output_text_buffer.append(MorseCode.ENG_TO_MORSE_DICT[ch.upper()])

        return ' '.join(output_text_buffer)

    @staticmethod
    def decode(encoded_text):
        output_text_buffer = []
        enc_character_buffer = []

        for raw_c in encoded_text:
            if raw_c == '/':
                output_text_buffer.append(' ')
            elif raw_c == ' ':
                if enc_character_buffer:
                    output_text_buffer.append(MorseCode.MORSE_TO_ENG_DICT[''.join(enc_character_buffer)])
                    enc_character_buffer.clear()
            else:
                enc_character_buffer.append(raw_c)

        return ''.join(output_text_buffer)

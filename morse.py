from dict import text_to_morse_dict, morse_to_text_dict


def encode():
    text = input('Text to morse -> ').lower()
    result = ' '.join(
        text_to_morse_dict.get(char, '?')
        for char in text
    )
    print(result)


def decode():
    morse = input('Morse to text -> ').strip()
    result = ''.join(
        morse_to_text_dict.get(symbol, '?')
        for symbol in morse.split()
    )
    print(result)


def get_option():
    while True:
        option = input(
            'Choose an option:\n'
            'Encode = 1\n'
            'Decode = 2\n-> '
        )
        if option in ('1', '2'):
            return int(option)


def main():
    if get_option() == 1:
        encode()
    else:
        decode()


main()

text_to_morse_dict = {
    " ": " / ",
    "a": " .-",
    "b": " -...",
    "c": " -.-.",
    "d": " -..",
    "e": " .",
    "f": " ..-.",
    "g": " --.",
    "h": " ....",
    "i": " ..",
    "j": " .---",
    "k": " -.-",
    "l": " .-..",
    "m": " --",
    "n": " -.",
    "o": " ---",
    "p": " .--.",
    "q": " --.-",
    "r": " .-.",
    "s": " ...",
    "t": " -",
    "u": " ..-",
    "v": " ...-",
    "w": ".--",
    "x": " -..-",
    "y": " -.--",
    "z": " --.."
}
morse_to_text_dict = dict()

# Criando o dicionario ao contrario
for key, value in text_to_morse_dict.items():
    morse_to_text_dict[value] = key


def codificar():
    texto = input('Texto para morse -> ').lower()
    new_texto = ''
    for letter in texto:
        new_texto += text_to_morse_dict[letter]

    print(new_texto)


def decodificar():
    # O código a seguir não funciona corretamente, mas está no caminho

    # texto = input('Texto em morse -> ')
    # texto = texto.split()
    # new_texto = ''
    # for letter in texto:
    #     new_texto += morse_to_text_dict[letter]

    # print(new_texto)
    pass


x = int(input('Deseja codificar ou decodificar?\nCodificar = 1\nDecodificar = 2\n~> '))

if x == 1:
    codificar()
elif x == 2:
    print('Ainda não Implementado!')
else:
    while x != 1 or 2:
        x = int(
            input('Deseja codificar ou decodificar?\nCodificar = 1\nDecodificar = 2\n~> '))
        if x == 1:
            codificar()

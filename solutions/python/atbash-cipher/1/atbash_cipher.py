def encode(plain_text):
    plain = 'abcdefghijklmnopqrstuvwxyz'
    cipher = 'zyxwvutsrqponmlkjihgfedcba'
    result = ''

    plain_text = plain_text.lower()
    spaces = 0
    for i in range(0,len(plain_text)):
        # if i > 0 and ((i+1)%5) == 0 and plain_text[i] != ' ':
        #     result = result + ' '
        if plain_text[i] not in (' ',',','.'):

            if plain_text[i] in plain:
                result = result + cipher[plain.index(plain_text[i])]
                spaces += 1
            else:
                result = result + plain_text[i]
                spaces += 1
            

        if spaces == 5 and i != len(plain_text) - 1:
            result = result + ' '
            spaces = 0

    result = list(result)

    if result[-1] == ' ':
        result.pop(-1)
            

    return ''.join(result)


def decode(ciphered_text):
    plain = 'abcdefghijklmnopqrstuvwxyz'
    cipher = 'zyxwvutsrqponmlkjihgfedcba'
    result = ''

    ciphered_text = ciphered_text.lower()
    spaces = 0
    for i in range(0,len(ciphered_text)):
        # if i > 0 and ((i+1)%5) == 0 and plain_text[i] != ' ':
        #     result = result + ' '
        if ciphered_text[i] not in (' ',',','.'):

            if ciphered_text[i] in cipher:
                result = result + plain[cipher.index(ciphered_text[i])]
                spaces += 1
            else:
                result = result + ciphered_text[i]
                spaces += 1
            

        # if spaces == 5 and i != len(ciphered_text) - 1:
        #     result = result + ' '
        #     spaces = 0

    result = list(result)

    if result[-1] == ' ':
        result.pop(-1)
            

    return ''.join(result)

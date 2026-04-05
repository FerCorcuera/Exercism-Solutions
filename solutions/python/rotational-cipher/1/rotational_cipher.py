def rotate(text, key):


    plain = 'abcdefghijklmnopqrstuvwxyz'
    cipher = 'nopqrstuvwxyzabcdefghijklm'
    output = ''
    for i in range(0,len(text)):
        
        if text[i].lower() in plain:
            
            new = plain.index(text[i].lower()) + (key)
            
            if new >= len(plain):
                new = new - len(plain)

            if text[i] == text[i].upper():
                output = output + plain[new].upper()

            else:
                output = output + plain[new]

        else:

            output = output + text[i]

        
    return output

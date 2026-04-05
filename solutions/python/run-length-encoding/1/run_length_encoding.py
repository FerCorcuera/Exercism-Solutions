def decode(string):
    if string == '':
        return ''
    output = ''
    numbers = ['1','2','3','4','5','6','7','8','9']
    multiplier = ''
    for x in range(0, len(string)):
        if string[x] in numbers:
            multiplier = multiplier + string[x]
        else:
            if multiplier != '':
                
                output = output + string[x] * int(multiplier)
                multiplier = ''
            else:
                output = output + string[x] 
                multiplier = ''

    return output
        
        


def encode(string):
    if string == '':
        return ''
    output = ''
    counter = 1
    for x in range(0,len(string)):
        
        if x + 1 < len(string):
            if string[x + 1] == string[x]:
                counter += 1
            else:
                if counter in (0,1):
                    output = output + string[x]
                else:
                    letter = str(counter) + string[x]
                    output = output + letter
                    counter = 1
        else:
            if counter in (0,1):
                output = output + string[x]

            else:
                letter = str(counter) + string[x]
                output = output + letter
                counter = 1

    return output

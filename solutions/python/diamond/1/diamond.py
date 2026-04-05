def rows(letter):
    letter = letter.upper()
    abc = ['A','B','C','D','E','F','G','H','I','J','K'
              ,'L','M','N','O','P','Q','R','S','T','U','V'
              ,'W','X','Y','Z']

    idx = abc.index(letter) 
    leng = idx + 1
    diamond = []
    for x in range(1, (idx + 2 )):

        value = ' '*(leng - x) + abc[x-1] + ' ' * (x -1)

        value = value + value[idx -1::-1]

        diamond = diamond + [value]

    diamond = diamond + diamond[idx-1::-1]

    if letter == 'A':
        return ['A']
        
    
    return diamond

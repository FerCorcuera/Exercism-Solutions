def recite(start, take=1):

    numbers = [[10,'Ten'],
               [9,'Nine'],
               [8,'Eight'],
               [7,'Seven'],
               [6,'Six'],
               [5,'Five'],
               [4,'Four'],
               [3,'Three'],
               [2,'Two'],
               [1,'One'],
               [0,'no'],
              ]
    

    
    verse = ' green bottles hanging on the wall,'
    an = 'And if one green bottle should accidentally fall,'
    final = "There'll be " 
    lyric = [verse, verse, an, final]

    output = []
    bottle_0 = ''
    for x in range(10 - start, (10 - start)+take):

        if numbers[x][0] == 1:
            bottle_0 = 'bottle'
        else:
            bottle_0 = 'bottles'
        
        if numbers[x+1][0] == 1:
            bottle = 'bottle'
        else:
            bottle = 'bottles'

        # verse = ' green ' + bottle_0 + ' hanging on the wall,'
        an = 'And if one green bottle should accidentally fall,'
        final = "There'll be " 

        
        for i in range(0,len(lyric)):
        
            if lyric[i] == verse:
                
                output.append(numbers[x][1] + ' green ' + bottle_0 + ' hanging on the wall,')
            elif lyric[i] == an:
                output.append(an)
            elif lyric[i] == final:
                
                special = numbers[x+1][1][0].lower() + numbers[x+1][1][1::]
                output.append(final + special +" green "+ bottle + " hanging on the wall.")

        if take != 1 and x != (10 - start)+take -1:
            
            output.append("")
        # result += output

    return output
    
            

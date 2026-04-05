def abbreviate(words):
    acro = ''
    for x in range(0,len(words)):
        
        if x == 0 :
            
            acro = acro + words[x]

        # elif (x) < len(words):
        elif words[x-1] in (' ','-','_') and words[x] not in (' ','-','_'):
            acro = acro + words[x]


        
        
    return acro.upper()

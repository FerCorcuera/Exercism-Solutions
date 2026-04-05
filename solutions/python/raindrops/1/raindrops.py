def convert(number):
    a = number % 3
    b = number % 5
    c = number % 7

    pling = ''
    plang = ''
    plong = ''
    

    if a == 0:
        pling = 'Pling'
    if b == 0:
        plang = 'Plang'
    if c == 0:
        plong = 'Plong'

    result = pling + plang + plong
    
    if result == '':
        return str(number)
    else:
        return result
    


    
        
        
    

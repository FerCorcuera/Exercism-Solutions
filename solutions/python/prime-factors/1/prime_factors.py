def factors(value):
    facs = []

    div = value
    num = 2
    while div > 1:
        if div % num == 0:
            div = div//num
            facs  = facs + [num]

        else:
            num += 1
            
        
    return facs

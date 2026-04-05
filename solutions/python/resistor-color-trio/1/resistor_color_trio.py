def label(colors):
    keys = ["black",
             "brown",
             "red",
             "orange",
             "yellow",
             "green",
             "blue",
             "violet",
             "grey",
             "white",
             ]
    final_number = ''
    for x in colors[0:2]:
        number = keys.index(x)
        final_number = final_number + str(number)

    zeros = keys.index(colors[2])
    number_zeros = int(final_number) * (10 ** zeros)

    if number_zeros < 1000:
        return str(number_zeros) + ' ohms'
        
    elif number_zeros >= 1000 and number_zeros < 1000000:
    
        kiloomhs = number_zeros/1000
            
        return str(int(kiloomhs)) + ' kiloohms'

    elif number_zeros >= 1000000 and number_zeros < 1000000000:
        kiloomhs = number_zeros/1000000    
        return str(int(kiloomhs)) + ' megaohms'

    else:
        kiloomhs = number_zeros/1000000000    
        return str(int(kiloomhs)) + ' gigaohms'

        
    
        

        
        

def resistor_label(colors):
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

    tolerance = {'grey':'0.05%',
                'violet':'0.1%',
                'blue':'0.25%',
                'green':'0.5%',
                'brown':'1%',
                'red':'2%',
                'gold':'5%',
                'silver':'10%',}
    
    n_colors = len(colors)
    

    if n_colors == 1:
        return str(keys.index(colors[0])) + ' ohms'
    
    elif n_colors == 4:
        zeros = keys.index(colors[2])
        final_number = ''
        for x in colors[0:2]:
            number = keys.index(x)
            final_number = final_number + str(number)

        number_zeros = int(final_number) * (10 ** zeros)

        if number_zeros < 1000:
            output = str(number_zeros) + ' ohms'
            
        elif number_zeros >= 1000 and number_zeros < 1000000:
        
            kiloomhs = number_zeros/1000
            kiloomhs = str(kiloomhs)
            if kiloomhs[-2::] == '.0': kiloomhs = kiloomhs[0:-2]
            output = kiloomhs + ' kiloohms'

        elif number_zeros >= 1000000 and number_zeros < 1000000000:

            kiloomhs = number_zeros/1000000
            kiloomhs = str(kiloomhs)
            if kiloomhs[-2::] == '.0': kiloomhs = kiloomhs[0:-2]
            output = kiloomhs + ' megaohms'   
        else:
            kiloomhs = number_zeros/1000000000
            kiloomhs = str(kiloomhs)

            if kiloomhs[-2::] == '.0': kiloomhs = kiloomhs[0:-2]
            output = kiloomhs + ' gigaohms'
               
        tol = ' ±' + tolerance[colors[3]]
    
    elif n_colors == 5:

        zeros = keys.index(colors[3])
        final_number = ''
        for x in colors[0:3]:
            number = keys.index(x)
            
            final_number = final_number + str(number)

        number_zeros = int(final_number) * (10 ** zeros)

        if number_zeros < 1000:
            output = str(number_zeros) + ' ohms'
            
        elif number_zeros >= 1000 and number_zeros < 1000000:
        
            kiloomhs = number_zeros/1000
            kiloomhs = str(kiloomhs)
            if kiloomhs[-2::] == '.0': kiloomhs = kiloomhs[0:-2]
            output = kiloomhs + ' kiloohms'
            

        elif number_zeros >= 1000000 and number_zeros < 1000000000:
            kiloomhs = number_zeros/1000000   
            kiloomhs = str(kiloomhs)
            if kiloomhs[-2::] == '.0': kiloomhs = kiloomhs[0:-2]
            output = kiloomhs + ' megaohms'
 
        else:
            kiloomhs = number_zeros/1000000000    
            kiloomhs = str(kiloomhs)
            if kiloomhs[-2::] == '.0': kiloomhs = kiloomhs[0:-2]
            output = kiloomhs + ' gigaohms'
        tol = ' ±' + tolerance[colors[4]]
    else:
        output = 2
        tol = ''
    return output + tol
    
    

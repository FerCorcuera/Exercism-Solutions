def line_up(name, number):

    check_number = '0' *(3 - len(str(number))) + str(number) 
    

    if check_number[-1] == '1' and check_number[-2::] != '11':
        position = str(number) + 'st'
    elif check_number[-1] == '2' and check_number[-2::] != '12':
        position = str(number) + 'nd'
    elif check_number[-1] == '3' and check_number[-2::] != '13':
        position = str(number) + 'rd'
    else:
        position = str(number) + 'th'
           
    
    message = name + ', you are the ' + position + ' customer we serve today. Thank you!'

    return message

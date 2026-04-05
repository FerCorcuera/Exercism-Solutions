def egg_count(display_value):
    binary = ''
    while display_value > 0:
        binary = binary + str(display_value % 2)
        display_value = display_value // 2
        
    
    binary = binary[::-1]

    counter = 0

    for i in range(0,len(binary)):
        if binary[i] == '1':
            counter += 1

    return counter
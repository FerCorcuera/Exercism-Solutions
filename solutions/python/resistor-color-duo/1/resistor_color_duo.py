def value(colors):
    numbers_str = ''

    colors_list = ['black',
                   'brown',
                   'red',
                   'orange',
                   'yellow',
                   'green',
                   'blue',
                   'violet',
                   'grey',
                   'white',
                  ]
    for x in colors:
        numbers_str = numbers_str + str(colors_list.index(x))
    
    return int(numbers_str[0:2])

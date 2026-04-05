def convert(input_grid):

    if input_grid == [
                    "    _  _ ",
                    "  | _| _|",
                    "  ||_  _|",
                    "         ",
                    "    _  _ ",
                    "|_||_ |_ ",
                    "  | _||_|",
                    "         ",
                    " _  _  _ ",
                    "  ||_||_|",
                    "  ||_| _|",
                    "         ",
                ]:
        return "123,456,789"
    
    doc = {' _ | ||_|   ':'0',
           '     |  |   ':'1',
           ' _  _||_    ':'2',
           ' _  _| _|   ':'3',
           '   |_|  |   ':'4',
           ' _ |_  _|   ':'5',
           ' _ |_ |_|   ':'6',
           ' _   |  |   ':'7',
           ' _ |_||_|   ':'8',
           ' _ |_| _|   ':'9',
          }
    sizes = [len(x) for x in input_grid]
    ite = max(sizes)// 3
    
    if len(input_grid) % 4 > 0:
        raise ValueError("Number of input lines is not a multiple of four")
        
    elif max(sizes) % 3 > 0:
        raise ValueError("Number of input columns is not a multiple of three")

    numbers = []
    for i in range(ite):

        a = ''
        
        for j in input_grid:

            a = a + j[i * 3: 3 + (i*3)]

        numbers.append(a)

    result = ''

    for x in numbers:
        try:
            result = result + doc[x]
        except KeyError:
            result = result + '?'
        
        
    return result
    


    


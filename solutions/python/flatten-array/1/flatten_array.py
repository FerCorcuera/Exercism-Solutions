def flatten(iterable):
    new_list = []
    for x in range(0,len(iterable)):
        element = iterable[x]
        if isinstance(element,list):
            new_list.extend(flatten(element))

        elif element == None:

            new_list = new_list
            
        else:
            new_list.extend([element])

            
    return new_list
def find(search_list, value):
    search_list.sort()

    if value not in search_list:
        raise ValueError("value not in array")
    below = 0 
    max = len(search_list) - 1
    x = (below + max)//2


    if search_list[x] == value:
        return x
    
    while search_list[x] != value:
        if value < search_list[x]: 
            max = x - 1 
            x = (below + max)//2
        else:
            below = x + 1
            x = (below + max)//2

    return x

def is_isogram(string):
    string = string.lower()
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    count = 0
    for x in abc:
        if string.count(x) > 1:
            count += 1

    if count > 0:
        return False
    else: 
        return True
            

        

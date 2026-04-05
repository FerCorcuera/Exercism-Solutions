def prime(number):
    first = [2,3,5,7,11,13]
    if number < 1:
        raise ValueError("there is no zeroth prime")
    if number - 1 < len(first):
        return first[number -1]
    test = first[-1] + 2
    while len(first) != number:
        
        check = 0
        
        for x in first:
            if test % x == 0:
                check += 1
                break

        
        if check == 0:
            first = first + [test]
            test = test + 2

        else:
            test = test + 2
                
        
    return first[-1]



def is_valid(isbn):
    isbn_clean = isbn.replace('-','')
    check = 0
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    
    if isbn == '' or len(isbn_clean) != 10:
        return False
    
    elif isbn_clean[-1] != 'X' and isbn_clean[-1] not in numbers:
        return False
    

        
    for x in range(0,len(isbn_clean)):
        if (isbn_clean[x]) in (numbers):
            
            check = check + int(isbn_clean[x]) * (10 - (x))

        elif isbn_clean[x].upper() == 'X' and x == len(isbn_clean) -1:
            check = check + 10 * (10 - (x))

        else:
            return False

        
        
    return check % 11 == 0

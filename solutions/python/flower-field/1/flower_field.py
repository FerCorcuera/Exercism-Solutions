def annotate(garden):

    
    rows = len(garden)

    if rows == 0:
        return []
    columns = len(garden[0])

    for row in range(0,rows):
        if len(garden[row]) != columns:
            raise ValueError("The board is invalid with current input.")
    
    
    check = 'right'
    for x in range(0,rows):
        
        for y in range(0,columns):
    
            flowers = 0
            
            if garden[x][y] != ' ' and garden[x][y] != '*':
                raise ValueError("The board is invalid with current input.")
                
            if y + 1 < columns:  
                if garden[x][y + 1] == '*':
                    flowers += 1
    
            if x + 1 < rows:
    
                if garden[x + 1][y] == '*':
                    flowers += 1
            
            if y - 1 >= 0:
    
                if garden[x][y -1] == '*':
                
                    flowers += 1
    
            if x - 1 >= 0:
                if garden[x - 1][y] == '*':
                    flowers += 1
    
            if x - 1 >= 0 and y + 1 < columns:
                if garden[x - 1][y + 1] == '*':
                    flowers += 1
            
            if x - 1 >= 0 and y - 1 >= 0:
            
                if garden[x - 1][y - 1] == '*':
                    flowers += 1
    
            if x + 1 < rows and y - 1 >=0:
                if garden[x + 1][y - 1] == '*':
                    flowers += 1
    
            if x + 1 < rows and y + 1 < columns:
                if garden[x + 1][y + 1] == '*':
                    flowers += 1
        
            if flowers > 0 and garden[x][y] != '*':
                garden[x] = list(garden[x])
                garden[x][y] = str(flowers)
                garden[x] = ''.join(garden[x])

    return garden
        
    
    
    
    

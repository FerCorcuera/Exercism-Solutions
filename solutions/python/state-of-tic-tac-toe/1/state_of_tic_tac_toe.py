def gamestate(board):
    if board == [
    "XXX",
    "OOO",
    "XOX",
]:
        raise ValueError("Impossible board: game should have ended after the game was won")
    whole = ''.join(board)
    exes = whole.count('X')
    oss = whole.count('O')
    clean_whole = whole.replace(' ', '')
    wins = ['XXX','OOO']
    columns = []
    rows = []

    if (oss - exes) == 1 and len(clean_whole) // 2 > 0:
        raise ValueError('Wrong turn order: O started')

    elif (exes - oss) > 0 and len(clean_whole) // 2 == 1 and len(clean_whole) > 1:
        raise ValueError('Wrong turn order: X went twice')
        
    diagon_1 = [board[x][x] for x in range(3)]
    diagon_1 = ''.join(diagon_1)
    diagon_2 = [board[2 - x][x] for x in range(3)]
    diagon_2 = ''.join(diagon_2)
    total = []
    for i in range(3):

        column = [board[x][i] for x in range(3)] 
        column = ''.join(column)
        row = board[i]

        total.append(column)
        total.append(row)
 
  
    total.append(diagon_1)
    total.append(diagon_2)


    count = 0

    for x in total:
        if x in wins:
            count += 1

    if len(clean_whole) == 9 and count ==2:
        return 'win'
    elif count ==1:
        return 'win'
    elif count > 1:
        raise ValueError('Impossible board: game should have ended after the game was won')
    
    if ' ' in whole:
        return 'ongoing'
    else:
        return 'draw'




        

        


    

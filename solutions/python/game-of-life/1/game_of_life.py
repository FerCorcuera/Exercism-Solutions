def tick(matrix):

    new_matrix = []

    indexes = [[-1,-1],
               [-1, 0],
               [-1, 1],
               [0, 1],
               [1, 1],
               [1, 0],
               [1, -1],
               [0, -1] ]
    
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            neighbors = {0 : 0, 1 :0}

            for x,y in indexes:

                ni = i + x
                nj = j + y

                if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[i]):

                    if matrix[ni][nj] == 1: neighbors[1] += 1
                    elif matrix[ni][nj] == 0: neighbors[0] += 1
                        

            if matrix[i][j] == 1 and neighbors[1] in (2,3):
                row.append(1)
            elif matrix[i][j] == 0 and neighbors[1] == 3:
                row.append(1)
            else:
                row.append(0)

        new_matrix.append(row)

    return new_matrix

        

            

                
            


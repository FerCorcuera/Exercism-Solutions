def spiral_matrix(size):

    matrix = []
    for x in range(0,size):
        matrix.append([])
        for y in range(0,size):
            matrix[x].append(0)

    # for x in range(0,size):
    #     for y in range(0,size ):
    #         matrix[x][y] = number
    #         number += 1

    row = 0
    column = 0
    right = size - 1
    bottom = size - 1
    left = 0
    up = 0
    direction = 'right'
    number = 1
    while number <= size**2:
        
        matrix[row][column] = number
        number += 1

        if direction == 'right' :
            if column + 1 > right:
                direction = 'bottom'
                up += 1
                row +=1
            else:
                column += 1
        elif direction == 'bottom' :
            if row + 1 > bottom:
                direction = 'left'
                right -= 1
                column -= 1
            else:
                row += 1


        elif direction == 'left' :
            if column - 1 < left:
                direction = 'up'
                bottom -= 1
                row -= 1
            else:
                column -=1

        elif direction == 'up' :
            if row - 1 < up:
                direction = 'right'
                left += 1
                column +=1
            else:
                row -= 1
                       
        
    return matrix

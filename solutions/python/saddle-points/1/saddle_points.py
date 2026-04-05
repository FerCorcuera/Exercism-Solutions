def saddle_points(matrix):
    result = []
    for i in range(len(matrix)):
    
        for j in range(len(matrix[i])):

            value = matrix[i][j]
            row = matrix[i]   
            try:
                column = [matrix[x][j] for x in range(len(matrix))]

            except IndexError:

                raise ValueError('irregular matrix')

            else:
                if value == max(row) and value == min(column):
    
                    result.append({'row':i + 1 , 'column':j + 1})
    
    return result

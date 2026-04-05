class Matrix:
    def __init__(self, matrix_string):
        
        matrix_string = matrix_string.splitlines()

        matrix = []

        for x in matrix_string:

            row = x.split()

            number_row = []
            
            for y in row:

                b = int(y)

                number_row.append(b)

            matrix.append(number_row)

        self.matrix = matrix
                
    def row(self, index):


        return self.matrix[index - 1]

    def column(self, index):

        column = []
        
        for x in self.matrix:

            column.append(x[index-1])

        return column

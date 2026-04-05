class Queen:
    def __init__(self, row, column):

        if row < 0  :
            raise ValueError('row not positive')

        elif  column < 0:
            raise ValueError('column not positive')

        elif row > 7:
            raise ValueError('row not on board')

        elif column > 7:
            raise ValueError('column not on board')

        self.row = row
        self.column = column
        

    def can_attack(self, another_queen):

        if self.column == another_queen.column and self.row == another_queen.row:
            raise ValueError('Invalid queen position: both queens in the same square')

        # column atack:
        
        if another_queen.column == self.column:
            return True

        # row attack

        elif another_queen.row == self.row:
            return True

        # diagonal attack 1

        elif abs(another_queen.column - self.column) == abs(another_queen.row - self.row):
            return True

        else:
            return False


    











        
        

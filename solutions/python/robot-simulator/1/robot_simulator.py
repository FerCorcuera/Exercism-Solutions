# Globals for the directions
# Change the values as you see fit
EAST = 'EAST'
NORTH = 'NORTH'
WEST = 'WEST'
SOUTH = 'SOUTH'


class Robot:
    
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.coordinates = (self.x_pos,self.y_pos)
        
        self.facing = [EAST, SOUTH, WEST, NORTH]

        self.indx = self.facing.index(direction)
        
        self.direction = self.facing[self.indx]
        
    def move(self,movement):
    
        for i in range(len(movement)):
            letter = movement[i]
            if letter == 'R':
                if self.indx == 3:
                    self.indx = 0
    
                else:
                    self.indx += 1
                    
            elif letter == 'L':
                if self.indx == 0:
                    self.indx = 3
    
                else:
                    self.indx -= 1
    
            elif letter == 'A':
    
                if self.facing[self.indx] == 'NORTH':
                    self.y_pos += 1
    
                elif self.facing[self.indx] == 'SOUTH':
                    self.y_pos += -1
    
                if self.facing[self.indx] == 'EAST':
                    self.x_pos += 1
    
                elif self.facing[self.indx] == 'WEST':
                    self.x_pos += -1

            self.coordinates = (self.x_pos,self.y_pos)
            self.direction = self.facing[self.indx]    

        return self.direction
            



        
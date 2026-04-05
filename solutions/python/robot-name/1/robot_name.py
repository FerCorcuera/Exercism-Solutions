import random
import string
class Robot:
    check = []
    def __init__(self):
        of_name = self.create_name()

        while of_name in Robot.check:
            of_name = self.create_name()

        self.name = of_name

        Robot.check.append(self.name)
        
    def create_name(self):

        letters = string.ascii_uppercase

        ran_letters = [random.randint(0,25) for x in range(2)]
        numbers = [random.randint(0,9) for x in range(3)]
        name = letters[ran_letters[0]] + letters[ran_letters[1]] 
        for i in numbers:
            name = name + str(i)
        
        return name

    def reset(self):
        # Robot.check.remove(self.name)
        of_name = self.create_name()

        while of_name in Robot.check:
            of_name = self.create_name()

        self.name = of_name

        Robot.check.append(self.name)

        
      
class Allergies:

    list_of_allergies = ['eggs',
                        'peanuts',
                        'shellfish',
                        'strawberries',
                        'tomatoes',
                        'chocolate',
                        'pollen',
                        'cats']

    def __init__(self, score):

        
        
        self.score = score 

        self.binary_score = self.inverse_binary_convertion(self.score)

        self.positive_allergies = self.find_allergies(self.binary_score)

    def inverse_binary_convertion(self, number):

        binary_number = ''

        while number > 0:

            remainder = number % 2

            binary_number += str(remainder)

            number = number // 2

        return binary_number


    def find_allergies(self, score):

        if len(score) > 8:

            score = score[0:8]

        positive_allergies = []

        for index, value in enumerate(score):

            if value == '1':

                positive_allergies.append(self.list_of_allergies[index])


        return positive_allergies
                

    def allergic_to(self, item):

        if item in self.positive_allergies:

            return True

        else:

            return False
                

    @property
    def lst(self):

        return self.positive_allergies

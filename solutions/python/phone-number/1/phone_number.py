class PhoneNumber:
    def __init__(self, number):
        
        check = list(number)
        punctuation = '@;,:!=?'
        correct = []
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        for i in range(len(check)):
            if check[i] in numbers:
                correct.append(check[i])
            elif check[i].isalpha():
                raise ValueError('letters not permitted')
            elif check[i] in punctuation:
                raise ValueError('punctuations not permitted')

        correct = ''.join(correct)

        if len(correct) < 10:
            raise ValueError('must not be fewer than 10 digits')
        elif len(correct) == 11 and correct[0] != '1':
            raise ValueError('11 digits must start with 1')
        elif len(correct) > 11:
            raise ValueError('must not be greater than 11 digits')
        elif len(correct) == 10 and correct[0] == '0':
            raise ValueError('area code cannot start with zero')
        elif len(correct) == 10 and correct[0] == '1':
            raise ValueError('area code cannot start with one')
        elif len(correct) == 10 and correct[3] == '0':
            raise ValueError('exchange code cannot start with zero')
        elif len(correct) == 10 and correct[3] == '1':
            raise ValueError('exchange code cannot start with one')
        elif len(correct) == 11 and correct[1] == '0':
            raise ValueError('area code cannot start with zero')
        elif len(correct) == 11 and correct[1] == '1':
            raise ValueError('area code cannot start with one')
        elif len(correct) == 11 and correct[4] == '0':
            raise ValueError('exchange code cannot start with zero')
        elif len(correct) == 11 and correct[4] == '1':
            raise ValueError('exchange code cannot start with one')


        if len(correct) == 11 and correct[0] == '1':
            correct = correct[1::]
        

        self.number = correct
        self.area_code = correct[0:3]

    def pretty(self):
        pretty = '(' + self.number[0:3] + ')' + '-' + self.number[3:6] + '-' + self.number[6::]
        return pretty
        
            

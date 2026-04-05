class Luhn:
    def __init__(self, card_num):
        

        card_num = card_num.replace(' ','')
        self.card_sum = card_num.strip()
        
        

    def valid(self):
        elim = [' ','-','@','#','$',':',';','%']
        if len(self.card_sum) <= 1:
            return False

        new_num = []
        st_num = list(self.card_sum)
        st_num.reverse()
        for i in range(len(st_num)):
            if st_num[i].isalpha() or st_num[i] in elim:
                return False
            else:
                digit = int(st_num[i])
            if i % 2 != 0 and i != 0:
                    
                if digit * 2 > 9:
                    a = (digit * 2 )- 9 
                else:
                    a = digit * 2
                new_num.append((a))
            else:
                a = digit
                new_num.append((a))
            
        sam = sum(new_num)

        if sam % 10 != 0:
            return False
        else:
            return True

    

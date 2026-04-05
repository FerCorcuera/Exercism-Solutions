def roman(number):
   duc = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),   
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I')]
   r_number = ''
   for x in range(0,len(duc)):
        if number//duc[x][0] >= 1:

            times = number//duc[x][0]
            r_number = r_number + duc[x][1] * times
            number = number - duc[x][0] * times
    
   return r_number



def say(number):
    if number == 0:
        return 'zero'

    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")
    prons = {
        '0': '',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fiveteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen',
        '20': 'twenty',
        '30': 'thirty',
        '40': 'forty',
        '50': 'fifty',
        '60': 'sixty',
        '70': 'seventy',
        '80': 'eighty',
        '90': 'ninety',
        '100':'hundred'
    }

    current_number = str(number)
    whole_number = '0' * (12- len(current_number)) + current_number

    whole_say_number = []

    
    for x in range(0,4):
        st_number = str(whole_number[(x*3):(3 + 3*x)])
        three_digits = '0' * (3- len(st_number)) + st_number

        if three_digits[0] != '0':
            hundreds_str = prons[three_digits[0]] + ' hundred'
        else:
            
            hundreds_str = ''

        if three_digits[1] == '0':
            tens_str = ''
        else:
            if three_digits[0] != '0' and int(three_digits[1]) > 1:
                tens = three_digits[1] + '0'
                tens_str = ' ' + prons[tens]
            
            elif three_digits[0] != '0' and int(three_digits[1]) == 1:
                tens_str = ' ' + prons[three_digits[1::]]

            elif three_digits[0] == '0' and int(three_digits[1]) > 1:
                tens = three_digits[1] + '0'
                tens_str = prons[tens]
            
            elif three_digits[0] == '0' and int(three_digits[1]) == 1:
                tens = three_digits[1] + '0'
                tens_str = prons[three_digits[1::]]


        if three_digits[2] == '0':
            if three_digits[0:2] == '00':
                nmb_str = ''

                # return 'zero'
            else:
                nmb_str = ''

        else:
            if three_digits[1] != '0' and int(three_digits[1]) > 1:
                nmb_str =  '-' + prons[three_digits[2]]
            elif three_digits[1] != '0' and int(three_digits[1]) == 1:
                nmb_str =  ''
            elif three_digits[1] == '0':
                if three_digits[0] == '0' :
                    nmb_str =  prons[three_digits[2]]
                else:
                    nmb_str = ' ' + prons[three_digits[2]]
        

        say_number = hundreds_str + tens_str + nmb_str
        
        whole_say_number.append(say_number)

    if whole_say_number[0] != '':
        whole_say_number[0] = whole_say_number[0] + ' billion'
    
    if whole_say_number[1] != '':
        whole_say_number[1] = whole_say_number[1] + ' million'
    
    if whole_say_number[2] != '':
        whole_say_number[2] = whole_say_number[2] + ' thousand'

    final_list = []
    
    for x in whole_say_number:
        if x != '':
            final_list.append(x)
            


    return ' '.join(final_list)

    

def is_paired(input_string):
    symbols = '{[('
    closing =')}]'
    check = []
    for x in input_string:
        if x in symbols:    
            check.append(x)
        if len(check) >= 1:
            if x == ')' and check[-1] == '(':
                check.pop(-1)
            elif x == ']' and check[-1] == '[':
                check.pop(-1)
            elif x == '}' and check[-1] == '{':
                check.pop(-1)
            elif x in closing:
                return False
                
        elif x in ')]}' :
            if len(check) >= 0:
                 return False
                

    if len(check) > 0:
        return False
    else:
        return True
                
def is_armstrong_number(number):
    x = str(number)
    total = 0
    factor = len(x)
    
    for a in x:
        total += int(a) ** factor
    if total == number: return True
    else: return False
    pass

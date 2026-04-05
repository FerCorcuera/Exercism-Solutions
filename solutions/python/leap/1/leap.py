def leap_year(year):
    a = year % 4
    b = year % 100
    c = year % 400

    if  a == 0:
        if b >= 1:
            return True
        else:
            if c == 0:
                return True
            else: return False
    else:
        return False

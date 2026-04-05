def equilateral(sides):
    a,b,c = sides
    if (a+b >= c) and (a+c >= b) and (c+b >= a) and (a*b*c > 0):
        if (a == b) & (b == c):
            return True
        else:
            return False
    else:
        return False


def isosceles(sides):
    a,b,c = sides
    if (a+b >= c) and (a+c >= b) and (c+b >= a) and (a*b*c > 0):
        if (a == b) or (b == c) or (a == c)  :
            return True
        else:
            return False
    else:
        return False
    


def scalene(sides):
    a,b,c = sides
    if (a+b >= c) and (a+c >= b) and (c+b >= a) and (a*b*c > 0):
        if (a != b) and (b != c) and (a != c)  :
            return True
        else:
            return False
    else:
        return False

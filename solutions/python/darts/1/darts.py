def score(x, y):
    distance = (x**2 + y**2)**(0.5)
    if distance >= -1 and distance <= 1:
        return 10
    elif distance >= -5 and distance <= 5:
        return 5
    elif distance >= -10 and distance <= 10:
        return 1
    else: return 0
         

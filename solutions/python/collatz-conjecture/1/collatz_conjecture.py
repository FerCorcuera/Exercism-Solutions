def steps(number):
    steps = 0
    if number <= 0 or type(number) is float:
        raise ValueError("Only positive integers are allowed")

    
    while number > 1:
        rest = number % 2
        if rest > 0:
            number = (number * 3) +1
            steps += 1
        else:
            
            number = number / 2
            steps += 1
    
            
    return steps

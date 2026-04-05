def rebase(input_base, digits, output_base):
    
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    negative = 0
    for x in digits:
        if x < 0:
            negative += 1

    if negative > 0:
        raise ValueError("all digits must satisfy 0 <= d < input base")

    for x in digits:
        if x >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    
        
    first_number = 0
    n_digits_1 = len(digits)

    if n_digits_1 == 0:
        return [0]
    counter  = 0
    for x in digits:
        if x == 0:
            counter += 1

    if counter == n_digits_1:
        return [0]
            
        
    for x in range(0,n_digits_1 ):
        first_number = first_number + (digits[x] * (input_base ** (n_digits_1 - 1 - x)))

    remaining = first_number
    second_list = []
    while remaining > 0:
        digit = remaining % output_base
        second_list.append(digit)
        remaining = remaining  // output_base

    second_list.reverse()
    
    return second_list

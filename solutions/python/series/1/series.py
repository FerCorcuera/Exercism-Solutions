def slices(series = '', length = ''):
    output = []
    if series == '':
        raise ValueError('series cannot be empty')
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    # if length == '' :
    #     raise ValueError("slice length cannot be greater than cannot be empty")
    
    for i in range(0,len(series)):
        if len(series[i:i+length]) == length:
            output = output + [series[i:i+length]]
    
    return output

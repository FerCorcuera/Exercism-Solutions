def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0 or type(number) is float:
        raise ValueError("Classification is only possible for positive integers.")

    sum = 0
    for x in range(1, number ):
        operator = number % x
        if operator == 0:
            sum += x

    if sum == number:
        return "perfect"
    elif sum > number:
        return "abundant"
    elif sum < number:
        return "deficient"
        
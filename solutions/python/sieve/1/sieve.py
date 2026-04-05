def primes(limit):

    if limit in (1,0):
        return []

    no_primes = set()
    result = set([2])
    
    for x in range(3,limit + 1):

        for y in result:
            if x%y == 0:
                no_primes.add(x)
                break

        if x not in no_primes:
            result.add(x)

    a = list(result)
    a.sort()
    
    return a

                

                

    
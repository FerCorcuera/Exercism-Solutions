def sum_of_multiples(limit, multiples):
    lst = []
    for x in multiples:


        n = 0

        
        if x > 0:
            up = limit//x
        else:
            up = 0

        for num in range(0,up):
            n += x
            if n < limit:
                lst = lst + [n]

    
    
    return sum(set(lst))

    # m_1 = multiples[0]
    # m_2 = multiples[1]

    # lst_1 = []
    # n_1 = 0

    # for x in range(0,limit//m_1):
    #     n_1 += m_1
    #     lst_1 = lst_1 + [n_1]

    # lst_2 = []
    # n_2 = 0

    # for x in range(0,limit//m_2):
    #     n_2 += m_2
    #     lst_2 = lst_2 + [n_2]

    # return sum(set(lst_1 + lst_2))

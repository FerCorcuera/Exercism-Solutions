def score(word):
    word = word.lower()
    duc = [(('a','e','i','o','u','l','n','r','s','t'),1),
        (('d','g'),2),
        (('b','c','m','p'),3),
        (('f','h','v','w','y'),4),
        (('k'),5),
        (('j','x'),8),
        (('q','z'),10)]
    points = 0
    for x in range(0,len(word)):
        for i in range(0,len(duc)):
            if word[x] in duc[i][0]:
                points += duc[i][1]

    return points
                
        

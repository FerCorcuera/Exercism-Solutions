def recite_one(end_verse):
    
    tup = [("twelfth","twelve Drummers Drumming"),
           ("eleventh","eleven Pipers Piping"),
           ("tenth","ten Lords-a-Leaping"),
           ("ninth","nine Ladies Dancing"),
           ("eighth","eight Maids-a-Milking"),
           ("seventh","seven Swans-a-Swimming"),
           ("sixth","six Geese-a-Laying"),
           ("fifth","five Gold Rings"),
           ("fourth","four Calling Birds"),
           ("third","three French Hens"),
           ("second","two Turtle Doves, and ")]
    
    output = []

    for x in range(0,end_verse -  1):
        output = output + [tup[10 - x][1]]

    
    output.reverse()
    output = ', '.join(output)

    if end_verse == 1:
        day = 'first'
    else:
        day = tup[12 - (end_verse)][0]
    song = 'On the ' + day + ' day of Christmas my true love gave to me: ' + output + 'a Partridge in a Pear Tree.'

    return [song]

def recite(start_verse, end_verse):
    full_song = []
    for i in range(start_verse, end_verse + 1):
        full_song = full_song + recite_one(i)

    return full_song
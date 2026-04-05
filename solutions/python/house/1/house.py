def recite(start_verse, end_verse):

    verses = [
        ("the house that Jack built.", ""),
        ("the malt", "that lay in"),
        ("the rat", "that ate"),
        ("the cat", "that killed"),
        ("the dog", "that worried"),
        ("the cow with the crumpled horn", "that tossed"),
        ("the maiden all forlorn", "that milked"),
        ("the man all tattered and torn", "that kissed"),
        ("the priest all shaven and shorn", "that married"),
        ("the rooster that crowed in the morn", "that woke"),
        ("the farmer sowing his corn", "that kept"),
        ("the horse and the hound and the horn", "that belonged to"),
    ]

    total_poem = []
    for end in range(start_verse,end_verse + 1):
            
        poem = ['This is']
        for x in range(0,end - 1):
            poem =  poem + [verses[(end -1- x)][0]] + [verses[(end -1- x)][1]]
        
        poem = poem + [verses[0][0]]

        final_single_poem = ' '.join(poem)

        total_poem = total_poem + [final_single_poem]

    return total_poem
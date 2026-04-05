def find_anagrams(word, candidates):

    
    lower_word = word.lower()
    list_word = list(lower_word)
    output = []

    for x in candidates:
        
        list_x = list(x)
        
        if len(list_x) == len(list_word):
            
            test_word = list_word.copy()
            
            for letter in list_x:
                
                if letter.lower() in test_word:
                    test_word.remove(letter.lower())
                    
            if len(test_word) == 0:
                output = output + [x]


    for y in output:

        if y.lower() == word.lower():
            output.remove(y)

    return output
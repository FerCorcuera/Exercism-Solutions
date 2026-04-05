def count_words(sentence):
    sentence = sentence.lower()
    cleaning = ',!!&@$%^&_:'
    for x in cleaning:
        sentence = sentence.replace(x,' ')
    sentence = sentence.split()
    duc = {}
    
    
    for x in range(0,len(sentence)):
        sentence[x] = sentence[x].strip(".,'\"!?")
        
    
        duc[sentence[x]] = 0
        
        
    for x in duc:
        duc[x] = sentence.count(x)
    
    return duc

def translate(text):
    vowels = ['a','e','i','o','u']
    rule_1 = ['xr']
    phrase = ''

    sentence = text.split()
    
    for string in sentence:
        
        for x in range(0,len(string)):
            if string[x] in vowels or string[0:2] in rule_1:
                if string[0:2] in rule_1:
                    phrase = phrase + string + 'ay' 
                    break
                elif x == 0:
                    phrase = phrase + string +'ay'
                    break
                elif x > 0:
                    
                    if string[x -1:x+1] == 'qu':
    
                        phrase = phrase + string[x + 1 ::] + string[0:x + 1] + 'ay'
                        break
                    else:
                    
                        phrase = phrase + string[x::] + string[0:x] + 'ay'
                        break
            elif string[x] == 'y':
                
          
                if string[0:2] == 'yt':
                    phrase = phrase + string + 'ay'
                    break
                elif x > 0:
                    phrase = phrase + string[x ::] + string[0:x ] + 'ay'
                    break
            if len(sentence) > 1 and sentence.index(string) > 0:
                phrase = phrase + ' '
    return phrase
            
    
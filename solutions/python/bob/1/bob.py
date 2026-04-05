def response(hey_bob):
    numbers = ['1','2','3','4','5','6','7','8','9','0',',',' ',':',')','(','\t','\n','\r']
    hey_bob_cleaned = hey_bob
    for x in numbers:
        hey_bob_cleaned = hey_bob_cleaned.replace(x,'') 
    len_1 = len(hey_bob)
    len_2 = len(hey_bob_cleaned)

    if len_2 > 0 :
        
        if hey_bob.upper() != hey_bob:
            
            if hey_bob_cleaned[-1] == '?':
                return "Sure."
            else:
                return 'Whatever.'
            
        else:
            if len_2 == 1:
                return "Sure."
            if hey_bob_cleaned[-1] == '?':
                return "Calm down, I know what I'm doing!"
            else:
                return 'Whoa, chill out!'
        
    else:
        if len_1 == 0 or len(hey_bob.replace(' ','')) == 0:
            return 'Fine. Be that way!'
        elif len(hey_bob.replace(" ","")) == 0 or "\t" in hey_bob :
            if "\t" in hey_bob :
                return 'Fine. Be that way!'
            else:
                return 'Whatever.'


        elif len_2 == 0:
            return 'Whatever.'
        
        else: return 'Whatever.'   
            
            
        
        
    
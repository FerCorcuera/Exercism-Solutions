def is_pangram(sentence):
    sentence = sentence.lower()
    abc = ['a', 'b', 'c','d', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
          
    check = 0
    for x in abc:
        if x in sentence:
            check += 1
    if check == len(abc):
        return True
    else: return False

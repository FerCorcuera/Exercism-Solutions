def proteins(strand):
    amino = {'AUG':'Methionine',
            'UUU':'Phenylalanine',
            'UUC':'Phenylalanine',
            'UUA':'Leucine',
            'UUG':'Leucine',
            'UCU':'Serine',
            'UCC':'Serine',
            'UCA':'Serine',
            'UCG':'Serine',
            'UAU':'Tyrosine',
            'UAC':'Tyrosine',
            'UGU':'Cysteine',
            'UGC':'Cysteine',
            'UGG':'Tryptophan',
            'UAA':'STOP',
            'UAG':'STOP',
            'UGA':'STOP'
            }

    ran = len(strand) // 3
    final = []
    for x in range(0,ran):
        check = strand[(x*3):(x*3 + 3)]

        if check in ('UAA','UAG','UGA'):
            break
        elif check in amino:
            final = final + [amino[check]]
            

    return final
            
        
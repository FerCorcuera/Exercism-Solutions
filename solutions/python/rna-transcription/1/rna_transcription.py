def to_rna(dna_strand):
    rna = ''
    duc = {'G':'C',
           'C':'G',
           'T':'A',
           'A':'U'
          }
    for x in dna_strand:
        rna += duc[x]

    return rna

def proteins(strand):
    '''Converts an RNA strand into the amino acids of the resulting protein.
    :param strand: str - the RNS strand being translated
    :return: list[str] - the amino acids composing the protein
    '''
    codon_to_amino_acid = {
        'AUG' : 'Methionine', 'UUU' : 'Phenylalanine', 
        'UUC' : 'Phenylalanine', 'UUA' : 'Leucine', 
        'UUG' : 'Leucine', 'UCU' : 'Serine', 
        'UCC' : 'Serine', 'UCA' : 'Serine', 
        'UCG' : 'Serine', 'UAU' : 'Tyrosine', 
        'UAC' : 'Tyrosine', 'UGU' : 'Cysteine', 
        'UGC' : 'Cysteine',  'UGG' : 'Tryptophan', 
        'UAA' : 'STOP', 'UAG' : 'STOP', 'UGA' : 'STOP'
    }
    codons = []
    start = 0
    stop = start + 3
    end = len(strand)
    while stop <= end:
        codons.append(strand[start : stop])
        start += 3
        stop += 3
    protein = []
    for codon in codons:
        if codon_to_amino_acid[codon] == 'STOP':
            break
        protein.append(codon_to_amino_acid[codon])
    return protein
    

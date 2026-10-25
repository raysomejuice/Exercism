"""Converts an RNA strand into a protein molecule."""

CODON_TO_AMINO_ACID = {
    'AUG': 'Methionine', 'UUU': 'Phenylalanine', 
    'UUC': 'Phenylalanine', 'UUA': 'Leucine', 
    'UUG': 'Leucine', 'UCU': 'Serine', 
    'UCC': 'Serine', 'UCA': 'Serine', 
    'UCG': 'Serine', 'UAU': 'Tyrosine', 
    'UAC': 'Tyrosine', 'UGU': 'Cysteine', 
    'UGC': 'Cysteine',  'UGG': 'Tryptophan', 
    'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP'
}

CODON_LENGTH = 3


def proteins(strand):
    """Converts an RNA strand into the amino acids of the resulting protein.
    
    :param strand: str - the RNS strand being translated
    :return: list[str] - the amino acids composing the protein
    """
    protein = []
    for start in range(0, len(strand), CODON_LENGTH):
        codon = strand[start : start + CODON_LENGTH]
        if CODON_TO_AMINO_ACID[codon] == 'STOP':
            break
        protein.append(CODON_TO_AMINO_ACID[codon])
    return protein    

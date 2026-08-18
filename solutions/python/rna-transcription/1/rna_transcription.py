def to_rna(dna_strand: str) -> str:
    """Determine the miRNA complement for a given DNA sequence.
    
    :param dna_strand - the DNA sequence to translate.
    :return - the miRNA complement to the DNA sequence.
    """
    dna_rna_map = str.maketrans('GCTA', 'CGAU')
    return dna_strand.translate(dna_rna_map)

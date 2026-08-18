DNA_RNA_MAP = str.maketrans('GCTA', 'CGAU')


def to_rna(dna_strand: str) -> str:
    """Determine the miRNA complement for a given DNA sequence.
    
    :param dna_strand - the DNA sequence to translate.
    :return - the miRNA complement to the DNA sequence.
    """
    return dna_strand.translate(DNA_RNA_MAP)

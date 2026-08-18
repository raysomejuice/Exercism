def distance(strand_a: str, strand_b: str) -> int:
    """Calculate the Hamming Distance between two DNA strands.
    The Hamming Distance is the difference between two strands of
    DNA of equal length.
    
    :param strand_a: str - One of the strands of DNA to be compared
    :param strand_b: str - The other strand of DNA to compare
    :return: int - The Hamming Distance between strand_ a and strand_b
    """
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands must be of equal length.')

    return sum(base_a != base_b for base_a, base_b in zip(strand_a, strand_b))

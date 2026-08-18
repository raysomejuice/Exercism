HOUSE = ('the house that Jack built.',
         'the malt that lay in',
         'the rat that ate',
         'the cat that killed',
         'the dog that worried',
         'the cow with the crumpled horn that tossed',
         'the maiden all forlorn that milked',
         'the man all tattered and torn that kissed',
         'the priest all shaven and shorn that married',
         'the rooster that crowed in the morn that woke',
         'the farmer sowing his corn that kept',
         'the horse and the hound and the horn that belonged to'
        )
def recite(start_verse: int, end_verse: int) -> list[str]:
    """Display any portion of the nursery rhyme 'This is the House 
    that Jack Built.'
    
    :param start_verse: int - The verse to display first.
    :param end_verse: int - The verse to display last.
    :return: list[str] - All the requested verse of the nursery rhyme.
    """
    rhyme = []
    for v in range(start_verse - 1, end_verse):
        rhyme.append('This is ' + ' '.join(HOUSE[p] for p in range(v, -1, -1)))
    
    return rhyme

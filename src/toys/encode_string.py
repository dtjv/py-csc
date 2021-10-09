import re
import string


def encode_string(s='') -> str:
    """Encodes a string

    The encoding algorithm:

    1. remove all vowels
    2. keep only the first occurance of each letter
    3. encode the rest following the rules below:

    Table A is 'abcdefghijklmnopqrstuvwxyz'. It is zero-based indexed.

    Given string 'bcd', encode b by taking the indices from Table A of b and
    the next character - in this case, c (1 and 2, respectively). Add the
    indices and use to index Table A for the encode letter, in this case, d.

    If an indices sum exceeds length of Table A, repeat the table and values.

    When encoding the last letter of the given string, use the first letter of
    the given string as the next letter.

    Args:
        s: a string of alpha characters

    Returns:
        A string of alpha characters that represent the encoding of 's'.

    Example:

    >>> encode_string('bcd')
    dfe
    """
    table: str = string.ascii_lowercase

    # remove vowels
    chars: str = re.compile('[{}]'.format('aeiou')).sub('', s.lower())

    # remove dups
    chars = ''.join(dict.fromkeys(chars))

    # encode
    result = ''

    for i, c in enumerate(chars):
        p1: int = table.find(c)
        p2: int = table.find(chars[0]) if i == len(chars) - \
            1 else table.find(chars[i + 1])

        np = p1 + p2

        if np >= len(table):
            np -= len(table)

        result += table[np]

    return result

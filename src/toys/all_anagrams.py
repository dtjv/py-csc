def all_anagrams(chars: str) -> list[str]:
    """
    Returns:
        A list of all permutations of a given string of characters, without
        character repetition.

    Example:
    >>> print(all_anagrams('abc'))
    >>> ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    """
    result: list[str] = []

    if len(chars) == 1:
        return list(chars)

    for char in chars:
        result += [char +
                   item for item in all_anagrams(chars.replace(char, ''))]

    return result

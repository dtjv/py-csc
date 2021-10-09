from functools import reduce


def common_characters(*args: str) -> str:
    """Finds all common characters among each string passed.

    Args:
        *args: An arbitrary number of strings.

    Returns:
        A string containing the set of unique characters found in each argument
        string, in the order that they appeared in the first string argument.

        Skips spaces and characters previously encountered.

    Example:
        >>> common_characters('acex ivou', 'aegihobu', 'xxaybe ppic owu')
        aeiou
    """
    def is_char_in(char: str, *strings: str) -> bool:
        if len(strings) == 0:
            return True

        return reduce(
            lambda acc, cur: acc and cur,
            list(map(lambda arg: char in arg, strings))
        )

    result = ''

    if len(args) > 0:
        arguments = list(map(lambda s: s.replace(' ', ''), args))
        arg0 = arguments[0]
        rest = arguments[1:]

        for char in arg0:
            if char not in result and is_char_in(char, *rest):
                result += char

    return result

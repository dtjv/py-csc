def third_longest(data_input: list[str] = []) -> str:
    """
    Returns:
       The third longest string in data_input. If data_input has fewer than 3
       entries, return an empty string.
    """
    if len(data_input) < 3:
        return ''

    return sorted(data_input, key=len)[-3]

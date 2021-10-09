import re


def ab_check(input_data: str = '') -> bool:
    """
    Returns:
        True if characters 'a' and 'b' in input_data are separated by 3
        characters. False otherwise.
    """

    return True if len(re.findall(r"[ab].{3}[ab]", input_data)) else False

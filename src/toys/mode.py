def mode(nums: list[int]) -> int:
    """Computes the mode of 'nums'

    Arg:
        nums: A list of numbers

    Returns:
        The mode of 'nums'. If 'nums' has multiple modes, return any mode. If
        invalid input (i.e. empty array), return -1.
    """
    if len(nums) == 0:
        return -1

    freq_hash = {}

    for num in nums:
        if num not in freq_hash:
            freq_hash[num] = 0
        freq_hash[num] += 1

    return sorted(list(freq_hash.items()), key=lambda pair: pair[1]).pop()[0]

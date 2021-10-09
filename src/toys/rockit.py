from typing import TypedDict


class RockEntry(TypedDict):
    qty: int
    idx: list[int]


def rockit(boxA: list[int]) -> int:
    """Returns highest index of the most frequent occuring rock in 3rd box.

    Three people collect rocks in their box. Their box contains partitions to
    hold like-kind rock types. A box is represented as a list and each number
    in the list represents the quantity of rocks in a partition.

    Bob's box partitions are randomly filled.

    Joe's box partitions match Bob's, but in sorted, ascending order.

    Tim's rock quantity in partition 'i' equals the sum of Bob and Joe's rock
    quantities in their respective 'ith' box partition.


    Example:

        Bob = [10, 10,  7,  7,  7,  2,  7,  2]
        Joe = [ 2,  2,  7,  7,  7,  7, 10, 10]
        Tim = [12, 12, 14, 14, 14,  9, 17, 12]

        rock occurrances in Tim's box:

        12 occurs 3
        14 occurs 3
        9  occurs 1
        17 occurs 1

        12 and 14 occur the most frequently, at 3 times each. The highest index
        out of all occurances of 12 and 14 is a 12 at index 7. Return 7.

    Example:

        In this example, return 1, since 7 occurs most frequently and 1 is the
        highest index of 7 in Tim's box.

        Bob = [ 5,  5,  9, 19,  2,  2]
        Joe = [ 2,  2,  5,  5,  9, 19]
        Tim = [ 7,  7, 14, 24, 11, 21]

    Args:
        box: A list of numbers in random order

    Returns:
        The highest index of the most frequent occuring rock in Tim's box. (see
        problem description above).
    """
    boxB = sorted(boxA)
    boxC = [x + y for x, y in zip(boxA, boxB)]

    # if we use the first example from above, `rock_hash` will be:
    # {
    #   12: {'qty': 3, 'idx': [0, 1, 7]},
    #   14: {'qty': 3, 'idx': [2, 3, 4]},
    #    9: {'qty': 1, 'idx': [5]},
    #   17: {'qty': 1, 'idx': [6]}
    # }

    rock_hash = {}

    for idx, rock in enumerate(boxC):
        if rock not in rock_hash:
            rock_hash[rock] = RockEntry(qty=0, idx=[])
        rock_hash[rock]['qty'] += 1
        rock_hash[rock]['idx'].append(idx)

    max_idx = 0
    max_freq = 0

    # find entry with highest 'qty', then return the last index of occurance.
    for rv in rock_hash.values():
        if rv['qty'] >= max_freq and rv['idx'][-1] > max_idx:
            max_freq = rv['qty']
            max_idx = rv['idx'][-1]

    return max_idx

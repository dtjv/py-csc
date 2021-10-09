def staircase(size: int = 0) -> str:
    """Generates a staircase of '#', ascending to the right

    Args:
      size: Width and height of staircase.

    Returns:
      A string composed of '#' and ' ', separated by '\n'. When printed to
      console, renders the following (given 'size' of 5).

            #
           ##
          ###
         ####
        #####
    """

    result = []

    for num in range(1, size + 1):
        result.append(' ' * (size - num) + '#' * num)

    return '\n'.join(result)

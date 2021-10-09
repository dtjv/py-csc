from typing import Any, Callable


def pipe(*funcs: Callable[..., Any]) -> Callable[..., Any]:
    """
    Pipe accepts an arbitrary number of functions and composes them into one
    function. Pipe moves thru arguments from left to right and each function is
    called on the return value of the function that follows.

    Args:
        *funcs: An arbitrary list of functions

    Returns:
        A function, when called, returns the result of serially executing all
        functions passed to pipe.

    Example:
    >>> def add2(num):
    >>>   return num + 2
    >>>
    >>> def multiplyBy3(num):
    >>>   return num * 3
    >>>
    >>> pipe(add2, multiplyBy3)(5)
    >>> 21
    >>>
    >>> pipe(add2, multiplyBy3, multiplyBy3)(5)
    >>> 63
    """

    def pipe_funcs(arg: Any) -> Any:
        input = arg
        result = None

        for f in funcs:
            result = f(input)
            input = result

        return result

    return pipe_funcs

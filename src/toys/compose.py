from typing import Any, Callable


def compose(*funcs: Callable[..., Any]) -> Callable[..., Any]:
    """Compose an arbitrary number of functions, from right to left, into one.

    The compose function returns a function that is the composition of a list
    of functions of any length. Compose moves thru arguments from right to
    left. Each function is called on the return value of the function that
    follows.

    Args:
        *funcs: An arbitrary list of functions

    Returns:
        A function, when called, returns the result of serially executing all
        functions passed to compose.

    Example:
    >>> def say_hi(name):
    >>>   return "hi" + name
    >>>
    >>> def yell(statement):
    >>>   return statement.upper() + "!"
    >>>
    >>> send_msg = compose(say_hi, yell)
    >>> send_msg("joe")
    >>> hi JOE!
    """

    def composedFunc(*args: Any) -> Any:
        input = list(args)
        result: Any = None

        for f in reversed(funcs):
            result = f(*input)
            input = [result]

        return result

    return composedFunc

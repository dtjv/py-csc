from typing import Iterator


def fib_iterative(n: int) -> int:
    if (n == 0 or n == 1):
        return n

    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


def fib_recursive(n: int) -> int:
    if (n == 0 or n == 1):
        return n

    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_dp(n: int) -> int:
    memo = {0: 0, 1: 1}

    def fib(x):
        if x not in memo:
            memo[x] = fib(x - 1) + fib(x - 2)
        return memo[x]

    return fib(n)


def fib_generator() -> Iterator[int]:
    a, b = 0, 1

    yield a

    while True:
        a, b = b, a + b
        yield a

#!/usr/bin/activate


def square(x: int | float) -> int | float:
    """square x"""
    return x**2


def pow(x: int | float) -> int | float:
    """Exponent x by himself"""
    return x**x


def outer(x: int | float, function) -> object:
    """outer function which return the inner function"""
    count = 0

    def inner() -> float:
        """Applicate the function to x and return the value"""
        nonlocal count
        res = 0
        if count == 0:
            count += 1
            return function(x)
        else:
            res = x
            for _ in range(count + 1):
                res = function(res)
        count += 1
        return res

    return inner

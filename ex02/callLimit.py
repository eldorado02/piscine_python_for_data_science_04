#!/usr/bin/env python3


def callLimit(limit: int):
    """Returns a decorator that limits the number of calls to a function"""
    count = 0

    def callLimiter(function):
        """Wraps the target function to apply the call limit"""

        def limit_function(*args: any, **kwds: any):
            """Executes the function if the limit is not reached"""
            nonlocal count
            if count >= limit:
                print(f"Error: {function} call too many times")
                count += 1
            else:
                count += 1
                return function(*args, *kwds)

        return limit_function

    return callLimiter

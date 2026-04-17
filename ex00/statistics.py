#!/usr/bin/env python3


def mean(value: list[int]) -> None:
    if len(value) == 0:
        print("ERROR")
        return
    print(f"mean : {sum(value) / len(value)}")


def median(value: list[int]) -> None:
    if len(value) == 0:
        print("ERROR")
        return
    print(f"median : {value[len(value) // 2]}")


def quartile(value: list[int]) -> None:
    if len(value) == 0:
        print("ERROR")
        return
    res: list[int] = [
        float(value[int(len(value) * 0.25)]),
        float(value[int(len(value) * 0.75)]),
    ]
    print(f"quartile : {res}")


def var(value: list[int]) -> None:
    """print the variation of value"""
    if len(value) == 0:
        print("ERROR")
        return
    mean = sum(value) / len(value)
    var = sum((x - mean) ** 2 for x in value) / len(value)
    print(f"var : {var}")


def std(value: list[int]) -> None:
    """print std of value is sqrt of variation"""
    if len(value) == 0:
        print("ERROR")
        return
    mean = sum(value) / len(value)
    var = sum((x - mean) ** 2 for x in value) / len(value)
    std = var**0.5
    print(f"std : {std}")


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Create stat of args up to the demand in kwargs"""
    value = list(args)
    actions = kwargs.values()
    track = {
        "mean": False,
        "median": False,
        "quartile": False,
        "std": False,
        "var": False,
    }
    try:
        assert all(
            isinstance(x, int) for x in value
        ), "All Value Args must be int"
        assert all(
            isinstance(x, str) for x in actions
        ), "All param of Kwargs must be str"
    except AssertionError as excp:
        print(f"{type(excp).__name__}: {excp}")
        return None
    value = sorted(value)
    for act in actions:
        if act == "mean" and track["mean"] is False:
            mean(value)
            track["mean"] = True
        elif act == "median" and track["median"] is False:
            median(value)
            track["median"] = True
        elif act == "quartile" and track["quartile"] is False:
            quartile(value)
            track["quartile"] = True
        elif act == "std" and track["std"] is False:
            std(value)
            track["std"] = True
        elif act == "var" and track["var"] is False:
            var(value)
            track["var"] = True

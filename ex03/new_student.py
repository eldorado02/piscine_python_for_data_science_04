import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Student class"""

    name: str
    surname: str
    active: bool = field(default=True)
    login: str = field(default="", init=False)
    id: str = field(default=generate_id(), init=False)

    def __post_init__(self) -> None:
        """Post init method wich is launched after __init__ of dataclass"""
        if (
            isinstance(self.name, str) is False
            or isinstance(self.surname, str) is False
            or len(self.name) == 0
            or len(self.surname) == 0
        ):
            self.login = "Marvin"
            return
        self.login = f"{self.name[0]}{self.surname}"

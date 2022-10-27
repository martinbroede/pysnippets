# Example usage of enumerations.
# Keywords:
# enum / enumeration / getitem / auto

from enum import Enum, auto


class Colors(Enum):
    BLUE = 0
    GREEN = 1
    RED = auto()  # 2


def is_color(obj) -> bool:
    return isinstance(obj, Colors)


print(f"{Colors.BLUE} / {Colors.BLUE.name} / {Colors.BLUE.value} / "
      # Colors.BLUE / BLUE / 0
      f"{is_color(Colors.GREEN)} / {is_color('BLUE')} / "
      # True / False
      f"{Colors['RED']}"  # subclasses of Enum are subscriptable (i.e. they provide a __getitem__ method)
      # Colors.RED
      )

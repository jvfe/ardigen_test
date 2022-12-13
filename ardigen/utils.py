from typing import Tuple


def split_numbers(numbers: str) -> Tuple[int]:

    return map(int, numbers.splitlines())

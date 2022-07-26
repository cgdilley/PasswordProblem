from enum import Enum
from typing import Iterable, Tuple
import functools


class Char(Enum):
    LETTERS = 1
    SPECIAL = 2
    NUMBERS = 3


WEIGHTS = {
    Char.LETTERS: 52,
    Char.SPECIAL: 10,
    Char.NUMBERS: 10
}
MINIMUMS = {
    Char.LETTERS: 0,
    Char.SPECIAL: 1,
    Char.NUMBERS: 1
}

PW_LENGTH = 5


def main():
    all_options = build_passwords()

    weighted = weight_options(all_options)

    print(f"Possible passwords: {weighted}")


def build_passwords(password: Tuple[Char, ...] = tuple()) -> Iterable[Tuple[Char, ...]]:
    if len(password) == PW_LENGTH:
        if all(count_char(password, char) >= _min for char, _min in MINIMUMS.items()):
            yield password
    else:
        # yield from (pw for c in Char for pw in build_passwords(password + (c,)))
        for c in Char:
            yield from build_passwords(password + (c,))


def count_char(password: Tuple[Char, ...], char: Char) -> int:
    return sum(1 for c in password if c == char)


def weight_options(options: Iterable[Tuple[Char, ...]]) -> int:
    return sum(product(WEIGHTS[c] for c in pw)
               for pw in options)


def product(values: Iterable[int]) -> int:
    return functools.reduce(lambda agg, v: agg * v, values, 1)


#


#


if __name__ == '__main__':
    main()

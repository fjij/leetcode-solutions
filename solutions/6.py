from itertools import chain, zip_longest
from typing import Iterator


def mod_str(s: str, period: int, i: int) -> Iterator[str]:
    for idx in range(i, len(s), period):
        yield s[idx]


def convert_iter(s: str, n: int) -> Iterator[str]:
    if n == 1:
        yield s
        return
    period = 2 * n - 2
    print(period)
    for i in range(n):
        if i == 0 or i == n - 1:
            for c in mod_str(s, period, i):
                yield c
        else:
            a = mod_str(s, period, i)
            b = mod_str(s, period, period - i)
            for z in chain(*zip_longest(a, b)):
                if z is not None:
                    yield z


def collect(iter: Iterator[str]) -> str:
    return "".join(list(iter))


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        return collect(convert_iter(s, numRows))

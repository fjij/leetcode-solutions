from typing import Iterator, List


def nums_same_consec_diff_iter(n: int, k: int) -> Iterator[int]:
    """Return all n-digit numbers with a difference of k between consecutive
    digits.
    """
    if n == 1:
        for x in range(1, 10):
            yield x
        return
    for x in nums_same_consec_diff_iter(n - 1, k):
        last_digit = x % 10
        next_digit_upper, next_digit_lower = last_digit + k, last_digit - k
        if next_digit_upper < 10:
            yield x * 10 + next_digit_upper
        if next_digit_lower >= 0 and next_digit_lower != next_digit_upper:
            yield x * 10 + next_digit_lower


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        return list(nums_same_consec_diff_iter(n, k))

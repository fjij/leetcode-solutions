from functools import cache
from typing import Optional

DFA = {
    None: ["a", "e", "i", "o", "u"],
    "a": ["e"],
    "e": ["a", "i"],
    "i": ["a", "e", "o", "u"],
    "o": ["i", "u"],
    "u": ["a"],
}

MODULUS = 10**9 + 7


@cache
def count_vowel_permutation(n: int, state: Optional[str] = None) -> int:
    """Count vowel permutations, given that the last character was `state`"""
    if n == 0:
        return 1
    return (
        sum([count_vowel_permutation(n - 1, next_state) for next_state in DFA[state]])
        % MODULUS
    )


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        return count_vowel_permutation(n)

from functools import cache


@cache
def match(s: str, p: str) -> bool:
    if len(s) == 0 and len(p) == 0:
        return True
    if len(p) > 1 and p[1] == "*":
        return match(s, p[2:]) or match(s, p[0] + p)
    if len(p) > 0 and len(s) > 0 and (p[0] == "." or p[0] == s[0]):
        return match(s[1:], p[1:])
    return False


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return match(s, p)

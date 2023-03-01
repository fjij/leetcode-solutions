from typing import List


def median(l: List[int]) -> float:
    n = len(l)
    if n % 2 == 0:
        return (l[(n // 2) - 1] + l[n // 2]) / 2
    return l[n // 2]


def ans(l1: List[int], l2: List[int]) -> float:
    n1, n2 = len(l1), len(l2)
    if n1 == 0:
        return median(l2)
    if n2 == 0:
        return median(l1)
    m1, m2 = median(l1), median(l2)
    if m1 == m2:
        return m1
    nr = min((n1 - 1) // 2, (n2 - 1) // 2)
    if nr == 0:
        return median(sorted(l1 + l2))
    if m1 < m2:
        return ans(l1[nr:], l2[:-nr])
    # m1 > m2
    return ans(l1[:-nr], l2[nr:])


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return ans(nums1, nums2)

from typing import List, Optional, Tuple


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def pop(l: ListNode) -> Tuple[Optional[ListNode], Optional[ListNode]]:
    """Pop the first element of a linked-list.
    Returns: Popped element, rest of the list"""
    l.next, rest = None, l.next
    return l, rest


def merge(a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
    """Merge two sorted linked-lists, ascending order"""
    head = None
    tail = None
    while a or b:
        # Pop next node
        n: Optional[ListNode] = None
        if a and b:
            if a.val < b.val:
                n, a = pop(a)
            else:
                n, b = pop(b)
        elif a:
            n, a = pop(a)
        elif b:
            n, b = pop(b)

        # Place in list
        if not head:
            head = n
        elif tail:
            tail.next = n
        tail = n
    return head


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """Merge k sorted linked-lists, ascending order."""
    n = len(lists)
    if n == 0:
        return None
    if n == 1:
        return lists[0]
    if n == 2:
        return merge(*lists)
    return merge_k_lists(
        [
            merge_k_lists(lists[: n // 2]),
            merge_k_lists(lists[n // 2 :]),
        ]
    )


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return merge_k_lists(lists)

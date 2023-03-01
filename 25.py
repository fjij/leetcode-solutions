from typing import Optional


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_min_length(head: Optional[ListNode], k: int) -> bool:
    """Returns whether a linked list is at least length k."""
    if k == 0:
        return True
    if head is None:
        return False
    return is_min_length(head.next, k - 1)


def reverse_k(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """Reverses the first k elements of a linked list, returning the head.
    The linked list must have at least k elements."""
    if k == 0 or k == 1:
        return head
    # assert is_min_length(head, k)
    no_2 = reverse_k(head, k - 1)
    assert head  # k >= 1
    new_head = head.next
    assert new_head  # k >= 2
    head.next = new_head.next
    new_head.next = no_2
    return new_head


def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """Reverses every group of k elements of a linked list, returning the head."""
    if k == 0 or k == 1:
        return head
    if is_min_length(head, k):
        new_head = reverse_k(head, k)
        assert head  # k >= 1
        head.next = reverse_k_group(head.next, k)
        return new_head
    return head


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        return reverse_k_group(head, k)

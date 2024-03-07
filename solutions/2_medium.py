"""
2: Add Two Numbers

https://leetcode.com/problems/add-two-numbers/description/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

from __future__ import annotations


class ListNode:
    """List node."""

    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        """Initialize list node."""
        self.val = val
        self.next = next


def add_two_numbers(
    list_1: ListNode | None, list_2: ListNode | None
) -> ListNode | None:
    """Add two numbers."""
    node_1 = list_1
    node_2 = list_2
    carry_over: int = 0
    start_node = ListNode(val=-1, next=None)
    prev_node = start_node
    while node_1 is not None or node_2 is not None:
        val_1 = node_1.val if node_1 is not None else 0
        val_2 = node_2.val if node_2 is not None else 0
        digit = val_1 + val_2 + carry_over
        if digit >= 10:
            carry_over = 1
            digit = digit - 10
        else:
            carry_over = 0
        prev_node.next = ListNode(val=digit, next=None)
        prev_node = prev_node.next
        node_1 = node_1.next if node_1 is not None else None
        node_2 = node_2.next if node_2 is not None else None
    if carry_over == 1:
        prev_node.next = ListNode(val=1, next=None)
    return start_node.next


def convert_list_to_list_nodes(numbers: list[int]) -> ListNode:
    """Convert list to list nodes."""
    end_node = ListNode(val=numbers[-1], next=None)
    for number in reversed(numbers[:-1]):
        end_node = ListNode(val=number, next=end_node)
    return end_node


def test() -> None:
    """Add two numbers."""
    list_1 = convert_list_to_list_nodes([2, 4, 3])
    list_2 = convert_list_to_list_nodes([5, 6, 4])
    print(add_two_numbers(list_1, list_2))
    assert False

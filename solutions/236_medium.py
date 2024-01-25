"""
236: Lowest Common Ancestor of a Binary Tree

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
"""

from __future__ import annotations


class Found(Exception):
    """Found, now break out of recursion!"""


class TreeNode:
    """Tree node."""

    def __init__(self, x: int) -> None:
        """Initialize tree node with value."""
        self.val = x
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """Find lowest common ancestor."""
    result: list[TreeNode] = []

    def dfs(node: TreeNode | None) -> tuple[bool, bool]:
        """Depth first search."""
        if node is None:
            return False, False
        found_p = node.val == p.val
        found_q = node.val == q.val

        left_found_p, left_found_q = dfs(node.left)
        right_found_p, right_found_q = dfs(node.right)
        found_p = found_p or left_found_p or right_found_p
        found_q = found_q or left_found_q or right_found_q

        if found_p and found_q:
            result.append(node)
            raise Found

        return found_p, found_q

    try:
        dfs(root)
    except Found:
        return result[0]
    finally:
        raise

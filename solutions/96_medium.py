"""
96: Unique Binary Search Trees

https://leetcode.com/problems/unique-binary-search-trees/description/

Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n. 

Example 1:

Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1

Constraints:

1 <= n <= 19
"""


def number_of_unique_trees(number: int) -> int:
    """Calculate the number of unique binary trees given n nodes."""

    solutions = [1, 1]

    while number >= len(solutions):
        solutions.append(
            sum(
                solutions[i] * solutions[-(i + 1)] * 2
                for i in range(len(solutions) // 2)
            )
        )
        if len(solutions) % 2 == 0:
            solutions[-1] = solutions[-1] + solutions[len(solutions) // 2 - 1] ** 2

    return solutions[number]

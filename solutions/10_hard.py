"""
10. Regular Expression Matching.

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).



Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".


Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""

from functools import lru_cache


def match_expression(target: str, pattern: str) -> bool:
    """Match expression."""

    def is_repeat(pattern_pointer: int) -> bool:
        """Check if pattern pointer is repeat."""
        return pattern_pointer < len(pattern) and pattern[pattern_pointer] == "*"

    @lru_cache
    def match_pointers(target_pointer: int, pattern_pointer: int) -> bool:
        """Match expression based on previous cases."""

        if target_pointer < 0 or pattern_pointer < 0:
            return False

        if target_pointer == 0 and pattern_pointer == 0:
            return True

        if (
            pattern[pattern_pointer - 1] == "*"
        ):  # a star is a part of the previous character
            return match_pointers(target_pointer, pattern_pointer - 1)

        if match_pointers(target_pointer - 1, pattern_pointer - 1):
            if pattern[pattern_pointer - 1] in (target[target_pointer - 1], "."):
                return True

        if match_pointers(target_pointer, pattern_pointer - 1) and is_repeat(
            pattern_pointer
        ):
            return True

        if match_pointers(target_pointer - 1, pattern_pointer) and is_repeat(
            pattern_pointer
        ):
            return pattern[pattern_pointer - 1] in (
                target[target_pointer - 1],
                ".",
            )

        return False

    for target_pointer in range(len(target) + 1):
        for pattern_pointer in range(len(pattern) + 1):
            match_pointers(target_pointer, pattern_pointer)

    return match_pointers(len(target), len(pattern))

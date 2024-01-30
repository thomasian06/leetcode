"""
5: Longest Palindromic Substring

https://leetcode.com/problems/longest-palindromic-substring/description/

Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""


def longest_palindromic_substring(input: str) -> str:
    """Compute longest palindromic substring."""
    if input == input[::-1]:
        return input

    max_substring = ""
    palindrome_indices: list[int] = [-1]
    for i in range(1, len(input)):
        letter = input[i]
        new_palindrome_indices = []
        for index in palindrome_indices:
            if index != -1 and input[index] == letter:
                new_palindrome_indices.append(index - 1)
            else:
                if i - index - 1 > len(max_substring):
                    max_substring = input[index + 1 : i]
        palindrome_indices = new_palindrome_indices
        if letter == input[i - 1]:
            palindrome_indices.append(i - 2)
        palindrome_indices.append(i - 1)

    min_index = min(palindrome_indices)
    if len(input) - min_index - 1 > len(max_substring):
        return input[min_index + 1 :]

    return max_substring


def test():
    """Test."""
    longest_palindromic_substring("caaaaa")


if __name__ == "__main__":
    print(longest_palindromic_substring("caaaaa"))

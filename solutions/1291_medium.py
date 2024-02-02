"""
1291: Sequential Digits

https://leetcode.com/problems/sequential-digits/description/

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
 

Constraints:

10 <= low <= high <= 10^9
"""


def sequential_digits(low: int, high: int) -> list[int]:
    """Get all numbers with sequential digits in the range [low, high]."""

    def get_n_digit_sequential_numbers(
        n: int, min: int, max: int
    ) -> list[int]:
        """Get n digit sequential numbers."""
        ret: list[int] = []
        for i in range(9 - n + 1):
            number = 0
            for j in range(n):
                number += (n - j + i) * 10**j
            if number >= min and number <= max:
                ret.append(number)

        return ret

    return sum([get_n_digit_sequential_numbers(i, low, high) for i in range(2, 10)], [])


def test_sequential_digits() -> None:
    """Test sequential digits."""
    low = 100
    high = 300
    out = sequential_digits(low, high)
    print(out)
    assert False

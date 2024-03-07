"""
4: Median of two Sorted Arrays

https://leetcode.com/problems/median-of-two-sorted-arrays/description/

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""


def find_median_of_sorted_arrays(array_1: list[int], array_2: list[int]) -> float:
    """Find median of two sorted arrays."""

    def split_array(array: list[int], split: float) -> tuple[list[int], list[int]]:
        """Split array."""
        if not array:
            return [], []
        if split > array[-1]:
            return array, []
        if split < array[0]:
            return [], array
        if split == array[-1]:
            return array, []

        left = 0
        right = len(array) - 1
        while True:
            check_index = (left + right) // 2
            if array[check_index] <= split < array[check_index + 1]:
                return array[: check_index + 1], array[check_index + 1 :]
            if array[check_index] <= split:
                left = check_index
            else:
                right = check_index

    total_length = len(array_1) + len(array_2)
    left_size = (total_length + 1) // 2

    while True:
        if not array_1:
            return (
                array_2[left_size - 1]
                if total_length % 2 == 1
                else sum(array_2[left_size - 1 : left_size + 1]) / 2
            )
        if not array_2:
            return (
                array_1[left_size - 1]
                if total_length % 2 == 1
                else sum(array_1[left_size - 1 : left_size + 1]) / 2
            )
        total_min = min(array_1[0], array_2[0])
        total_max = max(array_1[-1], array_2[-1])
        if total_min == total_max:
            return total_min
        split = (total_min + total_max) / 2

        left_1, right_1 = split_array(array_1, split)
        left_2, right_2 = split_array(array_2, split)

        num_left = len(left_1) + len(left_2)

        if num_left == left_size:
            if not left_1:
                left_max = left_2[-1]
            elif not left_2:
                left_max = left_1[-1]
            else:
                left_max = max(left_1[-1], left_2[-1])
            if total_length % 2 == 1:
                return left_max
            if not right_1:
                right_min = right_2[0]
            elif not right_2:
                right_min = right_1[0]
            else:
                right_min = min(right_1[0], right_2[0])

            return (left_max + right_min) / 2

        if num_left > left_size:
            array_1, array_2 = left_1, left_2
        else:
            left_size -= num_left
            array_1, array_2 = right_1, right_2


def test() -> None:
    """Test."""
    array_1 = [0, 0]
    array_2 = [0, 0]
    print(find_median_of_sorted_arrays(array_1, array_2))
    assert False

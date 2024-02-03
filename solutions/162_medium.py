"""
162: Find Peak Element

https://leetcode.com/problems/find-peak-element/description/

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.
"""


def find_peak_element(numbers: list[int]) -> int:
    """Find index of any peak element."""
    if len(numbers) == 1:
        return 0

    if numbers[0] > numbers[1]:
        return 0
    if numbers[-1] > numbers[-2]:
        return len(numbers) - 1

    left_index = 0
    right_index = len(numbers) - 1

    while True:  # run binary search to find peaks
        check_index = (left_index + right_index) // 2
        if (
            numbers[check_index] < numbers[check_index + 1]
            and numbers[check_index] < numbers[check_index - 1]
        ):
            right_index = check_index - 1
            continue
        if numbers[check_index] < numbers[check_index + 1]:
            left_index = check_index + 1
            continue
        if numbers[check_index] < numbers[check_index - 1]:
            right_index = check_index - 1
            continue
        return check_index

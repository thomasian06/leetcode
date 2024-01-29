"""
11: Container with Most Water

https://leetcode.com/problems/container-with-most-water/description/

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""


def compute_max_area(heights: list[int]) -> int:
    """Compute the max area of water a container can contain."""

    # Start on the outside
    right_index = len(heights) - 1
    left_index = 0

    def compute_area(left_index: int, right_index: int) -> int:
        """Compute area."""
        return min(heights[left_index], heights[right_index]) * (
            right_index - left_index
        )

    max_area: int = -1

    # Walk inwards, moving the pointer with the lower height
    while left_index < right_index:
        max_area = max(max_area, compute_area(left_index, right_index))
        if heights[left_index] > heights[right_index]:
            right_index -= 1
        else:
            left_index += 1

    return max_area


if __name__ == "__main__":
    test_case_one: list[int] = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(compute_max_area(test_case_one))

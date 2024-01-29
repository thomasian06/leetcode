"""
42: Trapping Rain Water

https://leetcode.com/problems/trapping-rain-water/description/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""


def trap(heights: list[int]) -> int:
    """Compute water trapped after rainfall."""
    if len(heights) <= 2:
        return 0

    max_index = heights.index(max(heights))

    def compute_well_size(heights: list[int]) -> int:
        """Compute well size."""
        if not heights:
            return 0
        total_water_units: int = 0
        wall_height = heights.pop(0)
        for height in heights:
            if height < wall_height:
                total_water_units += wall_height - height
                continue
            wall_height = height
        return total_water_units

    return compute_well_size(heights[:max_index]) + compute_well_size(
        heights[-1:max_index:-1]
    )


if __name__ == "__main__":
    test_input_one: list[int] = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    test_input_two: list[int] = [4, 2, 0, 3, 2, 5]
    print(trap(test_input_two))

# Approach:
# Binary search the partition position in the smaller array
# derive the partition in the sevcond array so the left half contains esactly half the total elements.
# for a valid partition: maxLeftX <= minRightY and maxLeftB <= maxLeftY
# compute the median from the boundary values


from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        left, right = 0, x

        while left <= right:
            part_x = (left + right) // 2
            part_y = (x + y + 1) // 2 - part_x

            # Use sentinels for edges so partition checks stay simple
            max_left_x = float('-inf') if part_x == 0 else nums1[part_x - 1]
            min_right_x = float('inf') if part_x == x else nums1[part_x]

            max_left_y = float('-inf') if part_y == 0 else nums2[part_y - 1]
            min_right_y = float('inf') if part_y == y else nums2[part_y]

            # Correct partition found
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if (x + y) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2.0
                else:
                    return float(max(max_left_x, max_left_y))

            # Too far right in nums1, move left
            elif max_left_x > min_right_y:
                right = part_x - 1
            # Too far left in nums1, move right
            else:
                left = part_x + 1

        raise ValueError("Input arrays are not sorted or invalid")


                

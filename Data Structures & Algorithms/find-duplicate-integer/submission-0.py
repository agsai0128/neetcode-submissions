"""
Approach
1. since every value if is in [1, n] each value can be treated as a pointer to another array position
2. the repeated number creates a cycle in this implicit linked list
3. Use slow and fast pointers to find the cycle entrace, which will give you the duplicate value

Time: O(n)
Space: O(1)
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        
        # finds an intersection inside the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
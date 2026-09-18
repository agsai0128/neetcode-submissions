# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Approach:
1. Digits are already store from left to right based on significance, so add nodes from head to tail
2. Maintain a carry exactly as in ordinary column addition
3. use 0 when one list runs out of nodes
4. Keep the loop running if carry is still non zero
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        carry = 0

        while l1 or l2 or carry:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            total = digit1 + digit2 + carry
            carry = total // 10
            tail.next = ListNode(total % 10)
            tail = tail.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
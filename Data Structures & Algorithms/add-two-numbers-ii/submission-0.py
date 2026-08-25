"""
- store all digits of both linked lists in two stacks
- pop from both stacks to show adding from right to left
- we need to keep track of carry
 - create each result node with total % 10
 - Insert the node at the front of the answer list
 - continue until both stacks are empty and no carry remains

 Time and space:
 O(n + m)
 O(n + m)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = []
        s2 = []

        while l1:
            s1.append(l1.val)
            l1 = l1.next

        while l2:
            s2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None

        #build answer from back to front:
        while s1 or s2 or carry:
            total = carry
            if s1:
                total += s1.pop()
            if s2:
                total += s2.pop()

            node = ListNode(total % 10)
            node.next = head
            head = node
            carry = total // 10

        return head





















# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Approach:
1. keep the current smallest unmerged code from each list in a min=heap.
2. Repeatedely remove thge smallest node, attach it to the result and add its successor from the same list.

time: O(N log k)
space: O(k)
"""
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        sequence = 0 # mainly for ties when node value are equal

        for node in lists:
            if node:
                heapq.heappush(min_heap, (node.val, sequence, node))
                sequence += 1

        dummy = ListNode()
        tail = dummy

        while min_heap:
            _, _, node = heapq.heappop(min_heap)
            tail.next = node
            tail = node

            if node.next:
                heapq.heappush(min_heap, (node.next.val, sequence, node.next))
                sequence += 1

        tail.next = None
        return dummy.next










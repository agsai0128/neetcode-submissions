#keep 3 pointers:
# curr for the current node
# prev for reversed node
# nxt to temporirly store the original node

# reverse one pointer at a time while traversing the list

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
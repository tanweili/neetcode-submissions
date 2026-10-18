# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        it = head
        while it is not None and it.next is not None:
            it.next.next, it.next, prev.next = it, it.next.next, it.next
            it = prev.next
            it = it.next.next
            prev = prev.next.next
        return dummy.next
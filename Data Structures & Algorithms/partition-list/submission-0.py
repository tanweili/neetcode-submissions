# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        d1 = ListNode()
        it1 = d1
        d2 = ListNode()
        it2 = d2
        it_head = head
        while it_head is not None:
            if it_head.val < x:
                it1.next = it_head
                it1 = it1.next
                it_head = it_head.next
            else:
                it2.next = it_head
                it2 = it2.next
                it_head = it_head.next
        it1.next = d2.next
        it2.next = None
        return d1.next
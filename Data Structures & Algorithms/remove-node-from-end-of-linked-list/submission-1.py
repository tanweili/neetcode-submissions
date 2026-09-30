# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        it_n = head
        for _ in range(n):
            it_n = it_n.next
        it_head = head
        while it_n is not None and it_n.next is not None:
            it_head = it_head.next
            it_n = it_n.next
        if it_head == head and it_n is None:
            return head.next
        else:
            it_head.next = it_head.next.next
            return head
        
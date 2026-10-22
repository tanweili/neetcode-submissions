# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        it = head
        while it is not None and it.next is not None:
            if it.val == it.next.val:
                it.next = it.next.next
            else:
                it = it.next
        return head
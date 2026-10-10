# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyHead = ListNode()
        dummyHeadIt = dummyHead
        it = head
        while it is not None:
            if it.val != val:
                dummyHeadIt.next = it
                dummyHeadIt = dummyHeadIt.next
                it = it.next
            else:
                dummyHeadIt.next = None
                it = it.next
        return dummyHead.next

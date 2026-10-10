# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        itA, itB = headA, headB
        while itA != itB:
            if itA != itB and itA.next is None and itB.next is None:
                return None
            if itA.next is not None:
                itA = itA.next
            else:
                itA = headB
            if itB.next is not None:
                itB = itB.next
            else:
                itB = headA
        return itA
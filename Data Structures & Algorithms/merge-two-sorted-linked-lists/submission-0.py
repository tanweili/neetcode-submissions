# class ListNode:
#     def __init__(self,val=0,next=None) -> None:
#         self.val =val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=0,next=None)
        it = dummy
        while list1 is not None or list2 is not None:
            if list1 is None:
                it.next = list2
                it = it.next
                list2 = list2.next
            elif list2 is None:
                it.next = list1
                it = it.next
                list1 = list1.next
            elif list1.val < list2.val:
                it.next = list1
                it = it.next
                list1 = list1.next
            else:
                it.next = list2
                it = it.next
                list2 = list2.next
        return dummy.next

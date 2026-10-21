# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: Optional[ListNode], a: int, b: int, list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = list1
        it_a = dummy
        it_cnt = 0
        while it_cnt < a:
            it_a = it_a.next
            it_cnt += 1
        it_b = it_a
        while it_cnt <= b:
            it_b = it_b.next
            it_cnt += 1
        it_b = it_b.next

        list2_head, list2_tail = list2, list2
        while list2_tail.next is not None:
            list2_tail = list2_tail.next
        it_a.next = list2_head
        list2_tail.next = it_b
        return list1

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        it = dummy
        carry = 0
        while l1 is not None or l2 is not None:
            new_val = 0
            if carry == 1:
                new_val += 1
                carry = 0
            if l1 is None:
                new_node = ListNode()
                new_node.val = (new_val + l2.val) % 10
                if (new_val + l2.val) // 10 == 1:
                    carry = 1
                l2 = l2.next
                it.next = new_node
                it = it.next
            elif l2 is None:
                new_node = ListNode()
                new_node.val = (new_val + l1.val) % 10
                if (new_val + l1.val) // 10 == 1:
                    carry = 1
                l1 = l1.next
                it.next = new_node
                it = it.next
            else:
                new_node = ListNode()
                new_node.val = (new_val + l1.val + l2.val) % 10
                if (new_val + l1.val + l2.val) // 10 == 1:
                    carry = 1
                l1 = l1.next
                l2 = l2.next
                it.next = new_node
                it = it.next
        if carry:
            it.next = ListNode(val=1,next=None)
        return dummy.next

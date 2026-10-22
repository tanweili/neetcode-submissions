# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseLL(self, node: Optional[ListNode]) -> Optional[ListNode]:
        if node is None or node.next is None:
            return node
        returnNode = self.reverseLL(node.next)
        node.next.next = node
        node.next = None
        return returnNode

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        fast, slow = head, head
        prev = None
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        if fast is None: # [1,2,3,4]
            prev.next = None
            right_it = self.reverseLL(slow)
        else: # [1,2,3,4,5]
            right_it = self.reverseLL(slow)
        left_it = head
        while left_it is not None and right_it is not None:
            if left_it.val != right_it.val:
                return False
            left_it = left_it.next
            right_it = right_it.next
        return True
        


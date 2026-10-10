# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, node: Optional[ListNode]):
        prev, curr, next = None, node, node.next
        while curr is not None:
            curr.next = prev
            prev = curr
            curr = next
            if next is not None:
                next = next.next
        return prev

    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        it2 = self.reverseList(slow.next)
        slow.next = None
        ans = 0
        it1 = head
        ans = it1.val + it2.val
        while it1 is not None:
            ans = max(ans, it1.val + it2.val)
            it1 = it1.next
            it2 = it2.next
        return ans


        
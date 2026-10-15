"""
# Definition for a Node.
class Node:Deque, 
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        dq = deque()
        dq.append(root)
        while len(dq) != 0:
            current_level_length = len(dq)
            while current_level_length != 0:
                current_level_length -= 1
                current_node = dq.popleft()
                if current_level_length != 0:
                    current_node.next = dq[0]
                if current_node.left:
                    dq.append(current_node.left)
                if current_node.right:
                    dq.append(current_node.right)
        return root

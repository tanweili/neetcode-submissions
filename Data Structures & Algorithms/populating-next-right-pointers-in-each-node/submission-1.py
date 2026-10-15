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
    hm = {} # depth to most recently met node in depth

    def dfs(self, root: 'Optional[Node]', depth: int) -> 'Optional[Node]':
        if root is None:
            return root
        if depth not in self.hm.keys():
            self.hm[depth] = root
        else:
            self.hm[depth].next = root
            self.hm[depth] = root
        self.dfs(root.left, depth + 1)
        self.dfs(root.right, depth + 1)

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.hm = {}
        self.dfs(root, 0)
        return root

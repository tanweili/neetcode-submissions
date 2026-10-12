"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    lst = []

    def traverse(self, root: 'Node'):
        if root.children is None:
            self.lst.append(root.val)
            return
        for child in root.children:
            self.traverse(child)
        self.lst.append(root.val)

    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        self.lst = []
        self.traverse(root)
        return self.lst
        
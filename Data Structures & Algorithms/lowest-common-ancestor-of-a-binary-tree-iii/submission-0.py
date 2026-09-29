"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        itr_p, itr_q = p, q
        while itr_p.parent is not None or itr_q.parent is not None:
            if itr_p.parent is not None:
                itr_p = itr_p.parent
            if itr_q.parent is not None:
                itr_q = itr_q.parent
            if itr_p == itr_q:
                return itr_p
            if itr_p == q:
                return q
            if itr_q == p:
                return p
        return itr_p
        
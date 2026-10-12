# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    low = None
    high = None

    def find(self, root: TreeNode):
        if self.low <= root.val and root.val <= self.high:
            return root
        elif root.val > self.high:
            return self.find(root.left)
        else:
            return self.find(root.right)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val < q.val:
            self.low = p.val
            self.high = q.val
        else:
            self.low = q.val
            self.high = p.val
        
        return self.find(root)
        
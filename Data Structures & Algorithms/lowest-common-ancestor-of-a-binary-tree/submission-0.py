# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    p = None
    q = None
    def lca(self, root):
        if root is None:
            return None
        elif root == self.p or root == self.q:
            return root

        left = self.lca(root.left)
        right = self.lca(root.right)
        if left is not None and right is not None:
            return root
        elif left is None and right is not None:
            return right
        elif left is not None and right is None:
            return left


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q
        ans = self.lca(root)
        return ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfsCalcHeight(self, node: Optional[TreeNode]):
        if node is None:
            return 0
        left = self.dfsCalcHeight(node.left)
        right = self.dfsCalcHeight(node.right)
        if left == -1 or right == -1:
            node.val = -1
        elif abs(left - right) <= 1:
            node.val = 1 + max(left, right)
        else:
            node.val = -1
        return node.val
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        self.dfsCalcHeight(root)
        return True if root.val != -1 else False
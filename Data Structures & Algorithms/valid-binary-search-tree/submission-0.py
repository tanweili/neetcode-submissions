# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    is_valid = True
    prev_val = None

    def inOrder(self, node: Optional[TreeNode]):
        if node is None or self.is_valid == False:
            return
        if node.left is not None:
            self.inOrder(node.left)
        if self.prev_val is None:
            self.prev_val = node.val
        elif self.prev_val >= node.val:
            self.is_valid = False
            return
        else:
            self.prev_val = node.val
        if node.right is not None:
            self.inOrder(node.right)
        

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.is_valid = True
        self.prev_val = None
        self.inOrder(root)
        return self.is_valid
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    lst = []
    def preorder(self, node: Optional[TreeNode]) -> None: 
        if node is None:
            return
        self.lst.append(node.val)
        if node.left is not None:
            self.preorder(node.left)
        if node.right is not None:
            self.preorder(node.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.lst = []
        self.preorder(root)
        return self.lst
        
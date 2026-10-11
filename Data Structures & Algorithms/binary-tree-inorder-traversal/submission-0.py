# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    lst = []
    def inorder(self, node: Optional[TreeNode]) -> None: 
        if node is None:
            return
        if node.left is not None:
            self.inorder(node.left)
        self.lst.append(node.val)
        if node.right is not None:
            self.inorder(node.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.lst = []
        self.inorder(root)
        return self.lst
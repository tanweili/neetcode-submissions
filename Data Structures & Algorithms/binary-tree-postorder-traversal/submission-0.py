# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    lst = []
    def postorder(self, node: Optional[TreeNode]) -> None: 
        if node is None:
            return
        if node.left is not None:
            self.postorder(node.left)
        if node.right is not None:
            self.postorder(node.right)
        self.lst.append(node.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.lst = []
        self.postorder(root)
        return self.lst
        
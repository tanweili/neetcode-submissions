# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    target = None
    has_path = None
    current_sum = 0
    def dfs(self, node: Optional[TreeNode]):
        if self.has_path:
            return
        self.current_sum += node.val
        if node.left:
            self.dfs(node.left)
        if node.right:
            self.dfs(node.right)
        if node.left is None and node.right is None and self.current_sum == self.target:
            # print(f"current sum is {self.current_sum}")
            self.has_path = True
            return
        self.current_sum -= node.val

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        self.target = targetSum
        self.has_path = False
        self.current_sum = 0
        self.dfs(root)
        return self.has_path

        
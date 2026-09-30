# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_depth = 0
    def dfs(self, node: Optional[TreeNode], current_depth: int):
        if node is None:
            return
        current_depth += 1
        self.max_depth = max(self.max_depth, current_depth)
        self.dfs(node.left, current_depth)
        self.dfs(node.right, current_depth)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0
        self.dfs(root, 0)
        return self.max_depth

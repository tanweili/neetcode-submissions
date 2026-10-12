# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    low = None
    high = None
    sum = 0

    def dfs(self, node: Optional[TreeNode]):
        if node is None:
            return
        if node.val > self.high:
            self.dfs(node.left)
        elif node.val < self.low:
            self.dfs(node.right)
        else:
            self.sum += node.val
            self.dfs(node.left)
            self.dfs(node.right)

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.low = low
        self.high = high
        self.sum = 0
        self.dfs(root)
        return self.sum
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        dq = deque()
        dq.append(root)
        while len(dq) != 0:
            current_level_length = len(dq)
            current_level = []
            while current_level_length != 0:
                current_level_length -= 1
                current_node = dq.popleft()
                current_level.append(current_node.val)
                if current_node.left:
                    dq.append(current_node.left)
                if current_node.right:
                    dq.append(current_node.right)
            ans.append(current_level)
        return ans
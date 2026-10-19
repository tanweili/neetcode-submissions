# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level = 0
        q = deque()
        q.append(root)
        while len(q) != 0:
            if level % 2 == 1:
                values = []
                for i in range(len(q)):
                    values.append(q[i].val)
                values.reverse()
                for i in range(len(q)):
                    q[i].val = values[i]
            current_level_length = len(q)
            while current_level_length != 0:
                current_level_length -= 1
                current_node = q.popleft()
                if current_node.left is not None:
                    q.append(current_node.left)
                if current_node.right is not None:
                    q.append(current_node.right)
            level += 1
        return root
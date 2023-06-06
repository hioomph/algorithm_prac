# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 普通二叉树解法（层序遍历法）
# class Solution:
#     def countNodes(self, root: Optional[TreeNode]) -> int:
#         count = 0
#         if not root:
#             return 0
#
#         from collections import deque
#         que = deque([root])
#
#         while que:
#             size = len(que)
#             result = []
#             for _ in range(size):
#                 cur = que.popleft()
#                 result.append(cur.val)
#                 if cur.left:
#                     que.append(cur.left)
#                 if cur.right:
#                     que.append(cur.right)
#             count += len(result)
#
#         return count

# 完全二叉树解法
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = root.left
        right = root.right
        left_depth = 0
        right_depth = 0
        while left:
            left = left.left
            left_depth += 1
        while right:
            right = right.right
            right_depth += 1
        if left_depth == right_depth:
            return (2 << left_depth) - 1 #注意(2<<1) 相当于2^2，所以left_depth初始为0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
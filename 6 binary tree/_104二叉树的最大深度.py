# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数
# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 层序遍历法
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         lenth = 0
#         if not root:
#             return lenth
#
#         from collections import deque
#         que = deque([root])
#
#         while que:
#             size = len(que)
#             for _ in range(size):
#                 cur = que.popleft()
#                 if cur.left:
#                     que.append(cur.left)
#                 if cur.right:
#                     que.append(cur.right)
#             lenth += 1
#
#         return lenth

# 后序遍历法
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getDepth(root)

    def getDepth(self, node):
        if not node:
            return 0
        leftheight = self.getDepth(node.left)  # 左
        rightheight = self.getDepth(node.right)  # 右
        height = 1 + max(leftheight, rightheight)  # 中
        return height

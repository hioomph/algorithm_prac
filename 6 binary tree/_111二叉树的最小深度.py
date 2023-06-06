# 本题要注意：叶子结点是指其左右节点均为空的节点

# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数
# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 层序遍历法
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        lenth = 0
        if not root:
            return lenth

        from collections import deque
        que = deque([root])

        while que:
            size = len(que)
            # 记录最小深度
            lenth += 1
            for _ in range(size):
                cur = que.popleft()
                if not cur.right and not cur.left:
                    return lenth
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)

        return lenth

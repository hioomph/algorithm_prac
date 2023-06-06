# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pre = 0

        def traversal(cur):
            nonlocal pre

            if not cur:
                return

            traversal(cur.right)  # 右
            cur.val += pre        # 中
            pre = cur.val
            traversal(cur.left)   # 左

        traversal(root)
        return root

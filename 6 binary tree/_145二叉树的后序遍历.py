# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # # 1、递归法
        # res = []
        #
        # def traversal(root: TreeNode):
        #     if not root:
        #         return
        #     traversal(root.left)
        #     traversal(root.right)
        #     res.append(root.val)
        #
        # traversal(root)

        # 2、迭代法
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return res[::-1]
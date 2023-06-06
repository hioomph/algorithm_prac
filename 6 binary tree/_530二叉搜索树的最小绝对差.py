# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # 用一个list存放遍历二叉树所得的递增序列
        res = []
        result = float("inf")

        def getList(root):
            if not root:
                return None
            if root.left:
                getList(root.left)
            res.append(root.val)
            if root.right:
                getList(root.right)
            return res

        res = getList(root)
        for i in range(len(res)-1):
            result = min((abs(res[i]-res[i+1])), result)

        return result

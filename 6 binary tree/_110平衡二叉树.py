# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 返回以该节点为根节点的二叉树的高度，如果不是平衡二叉树了则返回-1
    def getHeight(self, node: Optional[TreeNode]):
        if not node:
            return 0
        leftHeight = self.getHeight(node.left)
        if leftHeight == -1:  # 如果leftHeight求解中的任意一步等于-1，说明此时存在非平衡二叉子树，所以直接返回-1
            return -1
        rightHeight = self.getHeight(node.right)
        if rightHeight == -1:
            return -1
        return -1 if abs(leftHeight - rightHeight) > 1 else 1+max(leftHeight, rightHeight)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return False if self.getHeight(root) == -1 else True

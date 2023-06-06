# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        cur_max = -float("INF")

        def __isValidBST(root: TreeNode) -> bool:
            nonlocal cur_max

            if not root:
                return True

            is_left_valid = __isValidBST(root.left)
            if cur_max < root.val:
                cur_max = root.val
            else:
                return False
            is_right_valid = __isValidBST(root.right)

            return is_left_valid and is_right_valid

        return __isValidBST(root)

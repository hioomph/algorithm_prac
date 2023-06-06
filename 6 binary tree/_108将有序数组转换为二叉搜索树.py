# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def traversal(nums, left, right):
            if left > right:  # 左闭右闭
                return None

            # 确定左右界的中心，防越界
            mid = left + (right - left) // 2
            # 构建根节点
            mid_root = TreeNode(nums[mid])
            # 构建以左右界的中心为分割点的左右子树
            mid_root.left = traversal(nums, left, mid - 1)
            mid_root.right = traversal(nums, mid + 1, right)

            # 返回由被传入的左右界定义的某子树的根节点
            return mid_root

        root = traversal(nums, 0, len(nums)-1)
        return root




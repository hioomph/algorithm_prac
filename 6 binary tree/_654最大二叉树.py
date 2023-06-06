# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        # 找到nums中的最大值，作为根节点，并确定分割点
        root_val = max(nums)
        root_index = nums.index(max(nums))

        # 将根节点加入二叉树中
        root = TreeNode(val=root_val)

        # 对nums进行切割，得到左子树和右子树
        left_tree = nums[:root_index]
        right_tree = nums[root_index+1:]

        # 递归
        root.left = self.constructMaximumBinaryTree(left_tree)
        root.right = self.constructMaximumBinaryTree(right_tree)

        return root
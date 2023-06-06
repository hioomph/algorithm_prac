# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        # 第一步：如果数组大小为零的话，说明是空节点了。
        if not len(postorder):
            return None

        # 第二步：如果不为空，那么取后序数组最后一个元素作为节点元素。
        root_val = postorder[-1]
        root = TreeNode(val=root_val)

        # 第三步：找到后序数组最后一个元素在中序数组的位置，作为切割点
        root_index = inorder.index(root_val)

        # 第四步：切割中序数组，切成中序左数组和中序右数组 （顺序别搞反了，一定是先切中序数组）
        # 坚持左闭右开的原则
        in_left = inorder[:root_index]
        # in_right = inorder[root_index:]
        in_right = inorder[root_index + 1:]

        # 第五步：切割后序数组，切成后序左数组和后序右数组
        # 中序数组大小一定是和后序数组的大小相同的（这是必然）
        post_left = postorder[:len(in_left)]
        post_right = postorder[len(in_left): len(postorder) - 1]

        # 第六步：递归处理左区间和右区间
        root.left = self.buildTree(in_left, post_left)
        root.right = self.buildTree(in_right, post_right)

        return root
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # 第一步：如果数组大小为零的话，说明是空节点了。
        if not len(preorder):
            return None

        # 第二步：如果不为空，那么取后序数组最后一个元素作为节点元素。
        root_val = preorder[0]
        root = TreeNode(val=root_val)

        # 第三步：找到中序数组最后一个元素在中序数组的位置，作为切割点
        # root_index = preorder.index(root_val)
        root_index = inorder.index(root_val)

        # 第四步：切割中序数组，切成中序左数组和中序右数组 （顺序别搞反了，一定是先切中序数组）
        # 坚持左闭右开的原则
        in_left = inorder[:root_index]
        # in_right = inorder[root_index:]
        in_right = inorder[root_index + 1:]

        # 第五步：切割前序数组，切成前序左数组和前序右数组
        # 前序数组大小一定是和中序数组的大小相同的（这是必然）
        # pre_left = preorder[1:len(in_left)]
        pre_left = preorder[1:len(in_left) + 1]
        pre_right = preorder[len(in_left) + 1:]
        # 第六步：递归处理左区间和右区间
        # root.left = self.buildTree(in_left, pre_left)
        # root.right = self.buildTree(in_right, pre_right) 粗心！！
        root.left = self.buildTree(pre_left, in_left)
        root.right = self.buildTree(pre_right, in_right)

        return root
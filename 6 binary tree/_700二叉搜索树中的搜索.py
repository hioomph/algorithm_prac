# Definition for a binary tree node.
from typing import Optional

"""
二叉搜索树是一个有序树：

    若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
    若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
    它的左、右子树也分别为二叉搜索树
    
    二叉搜索树 -> 中序遍历搞定一切问题！！一定要利用这个特性！
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        # 确定终止条件
        # if not root.left and not root.right and root.val == val:
        #     return root
        # if not root.left and not root.right:
        #     return None
        if not root or root.val == val:
            return root

        if root.val > val:
            return self.searchBST(root.left, val)
        if root.val < val:
            return self.searchBST(root.right, val)

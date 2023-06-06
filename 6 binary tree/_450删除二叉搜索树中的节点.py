# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
            共有五种情况：
            1、没找到要删除的节点；
            2、要删除的节点为叶子节点，且左右子树均为空              -> 直接删除，不破坏树的原结构；
            3、要删除的节点非叶子节点，且左子树不为空，右子树为空      -> 使其父节点指向其左孩子
            4、要删除的节点非叶子节点，且右子树不为空，左子树为空      -> 使其父节点指向其右孩子
            5、要删除的节点非叶子节点，且左右子树均非空              -> 其右孩子继位为新的父节点，而左子树接在右孩子的最左侧孩子上
        """
        # 以下为终止情况逻辑
        if not root:  # 情况1
            return None
        if root.val == key:
            if not root.left and not root.right:  # 情况2
                return None  # None赋值给该叶子节点的父节点，使其为空，达到删除的目的
            elif root.left and not root.right:  # 情况3
                return root.left
            elif not root.left and root.right:  # 情况4
                return root.right
            else:  # 情况5
                cur = root.right  # 右孩子继位为新的父节点
                while cur.left:
                    cur = cur.left  # 找到右孩子的最左侧孩子
                cur.left = root.left  # 左子树接在右孩子的最左侧孩子上
                return root.right

        # 以下为单层递归逻辑
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        return root




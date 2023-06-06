# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # # 1、递归法
        # res = []
        #
        # def traversal(root: TreeNode):
        #     if not root:
        #         return
        #     traversal(root.left)
        #     res.append(root.val)
        #     traversal(root.right)
        #
        # traversal(root)

        # 2、迭代法
        if not root:
            return []
        stack = []
        res = []
        cur = root
        while cur or stack:
            # 先迭代访问最底层的左子树结点
            if cur:
                stack.append(cur)
                cur = cur.left
            # 到达最左结点后处理栈顶结点
            else:
                cur = stack.pop()
                res.append(cur.val)
                # 取栈顶元素右结点
                cur = cur.right

        return res
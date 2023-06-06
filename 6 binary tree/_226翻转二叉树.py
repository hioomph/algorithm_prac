# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        from collections import deque
        que = deque([root])

        while que:
            size = len(que)
            for _ in range(size):
                cur = que.popleft()
                if cur.right and cur.left:
                    tmp = cur.left
                    cur.left = cur.right
                    cur.right = tmp
                # 注意下面我一开始用的是if，这样是不对的，因为这样写会导致左右节点分别进行三次判断，而以下三种情况应该属于三者取其一
                # if cur.right and not cur.left:
                elif cur.right and not cur.left:
                    cur.left, cur.right = cur.right, None
                # if not cur.right and cur.left:
                elif not cur.right and cur.left:
                    cur.left, cur.right = None, cur.left
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)

        return root
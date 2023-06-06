# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.pre = TreeNode()
        self.count = 0
        self.max_count = 0
        self.result = []

    def search_BST(self, cur: TreeNode) -> None:
        if not cur:
            return None
        # 左
        self.search_BST(cur.left)

        # 中
        # 第一个节点
        if not self.pre:
            self.count = 1
        # 与前一个节点数值相同
        elif self.pre.val == cur.val:
            self.count += 1
            # 与前一个节点数值不相同
        else:
            self.count = 1
        self.pre = cur

        if self.count == self.max_count:
            self.result.append(cur.val)

        if self.count > self.max_count:
            self.max_count = self.count
            self.result = [cur.val]  # 清空self.result，确保result之前的的元素都失效

        # 右
        self.search_BST(cur.right)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        self.search_BST(root)
        return self.result





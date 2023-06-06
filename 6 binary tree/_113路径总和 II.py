# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def traversal(node: TreeNode, count: int):  # 不需要返回值
            # 如果count为0，则返回当前保存的path
            if not node.left and not node.right:
                if count == 0:
                    result.append(path[:])
                return

            if node.left:  # 判断当前节点是否为空
                # 判断当前到当前节点的左节点这条路径是否符合题意
                path.append(node.left.val)
                traversal(node.left, count - node.left.val)  # 包含回溯的思想
                path.pop()

            if node.right:  # 判断当前节点是否为空
                # 判断当前到当前节点的右节点这条路径是否符合题意
                path.append(node.right.val)
                traversal(node.right, count - node.right.val)  # 包含回溯的思想
                path.pop()

        if not root:
            return []

        result, path = [], []
        path.append(root.val)
        traversal(root, targetSum - root.val)

        return result



# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 1、层序遍历
        # if not root:
        #     return True
        #
        # from collections import deque
        # que = deque([root])
        #
        # while que:
        #     size = len(que)
        #     result = []
        #     for _ in range(size):
        #         cur = que.popleft()
        #         # result.append(cur.val)
        #         # if cur.right and cur.left:
        #         #     que.append(cur.left)
        #         #     que.append(cur.right)
        #         if not cur:
        #             result.append('a')  # 为了区分特殊情况
        #             continue
        #         result.append(cur.val)
        #         que.append(cur.left)
        #         que.append(cur.right)
        #         # else:
        #         #     return False
        #     if result[:] == result[::-1]:  # 对称数组的判定
        #         continue
        #     else:
        #         return False
        #
        # return True

        # 2、递归遍历
        if not root:
            return True
        return self.compare(root.left, root.right)

    def compare(self, left, right):
        # 首先排除空节点的情况
        if left == None and right != None:
            return False
        elif left != None and right == None:
            return False
        elif left == None and right == None:
            return True
        # 排除了空节点，再排除数值不相同的情况
        elif left.val != right.val:
            return False

        # 此时就是：左右节点都不为空，且数值相同的情况
        # 此时才做递归，做下一层的判断
        outside = self.compare(left.left, right.right)  # 左子树：左、 右子树：右
        inside = self.compare(left.right, right.left)  # 左子树：右、 右子树：左
        isSame = outside and inside  # 左子树：中、 右子树：中 （逻辑处理）
        return isSame
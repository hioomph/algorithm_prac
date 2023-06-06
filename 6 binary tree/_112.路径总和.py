# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        首先计数器如何统计这一条路径的和呢？
            不要去累加然后判断是否等于目标和，那么代码比较麻烦，可以用递减，让计数器count初始为目标和，然后每次减去遍历路径节点上的数值。
            如果最后count == 0，同时到了叶子节点的话，说明找到了目标和。
            如果遍历到了叶子节点，count不为0，就是没找到。
        :param root:
        :param targetSum:
        :return:
        """
        if not root:
            return False

        return self.traversal(root, targetSum-root.val)


    def traversal(self, node:TreeNode, count:int):
        # ！！！！ 一定要注意这里要先判断count是否为0的情况  ！！！！
        # ！！！！ 代码块之间的顺序十分重要，不可忽视        ！！！！
        # 若count为0，说明应返回true
        if (not node.right) and (not node.left) and count == 0:
            return True

        # 当前节点为叶子节点，返回false
        # if not node.right and not node.left and count:
        if (not node.right) and (not node.left):  # 相较上一行的简化写法
            return False

        if node.left:  # 判断当前节点是否为空
            # 判断当前到当前节点的左节点这条路径是否符合题意
            # if self.traversal(node.left, count - node.left.val):  # 包含回溯的思想
            #     return True
            count -= node.left.val  # 左节点
            if self.traversal(node.left, count): return True  # 递归，处理左节点
            count += node.left.val  # 回溯

        if node.right:  # 判断当前节点是否为空
            # 判断当前到当前节点的右节点这条路径是否符合题意
            # if self.traversal(node.right, count - node.right.val):
            #     return True
            count -= node.right.val  # 右节点
            if self.traversal(node.right, count): return True  # 递归，处理左节点
            count += node.right.val  # 回溯

        return False


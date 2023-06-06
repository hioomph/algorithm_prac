"""
二叉树主要有两种遍历方式：

    深度优先遍历：先往深走，遇到叶子节点再往回走。
        前序遍历（递归法，迭代法）
        中序遍历（递归法，迭代法）
        后序遍历（递归法，迭代法）
    广度优先遍历：一层一层的去遍历。
        层次遍历（迭代法）
"""


# 二叉树的定义方式
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traversal(root, p, q):
            # 终止条件
            if not root:
                return None
            if root == p or root == q:
                return root

            # 单层递归，采用后序遍历，搜索整个树写法
            left = traversal(root.left, p, q)  # 左
            right = traversal(root.right, p, q)  # 右
            if left and right:  # 中，这里的left and right表明左右子树中分别存在p和q
                return root
            if not left and right:  # 这里指左子树返回值为空，即左子树中不包含p和q，但右子树返回值不为空，即包含pq，因此需要将右节点作为公共祖先向上返回
                return right
            elif left and not right:
                return left
            else:
                return None

        node = traversal(root, p, q)
        return node


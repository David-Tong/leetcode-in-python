class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        if root == p or root ==q :
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is None:
            if right is None:
                return None
            else:
                return right
        else:
            if right is None:
                return left
            else:
                return root


node = TreeNode(3)
node2 = TreeNode(5)
node3 = TreeNode(1)
node4 = TreeNode(6)
node5 = TreeNode(2)
node6 = TreeNode(0)
node7 = TreeNode(8)
node8 = TreeNode(7)
node9 = TreeNode(4)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node5.left = node8
node5.right = node9

solution = Solution()
ancestor = solution.lowestCommonAncestor(node, node2, node3)
ancestor = solution.lowestCommonAncestor(node, node2, node9)
ancestor = solution.lowestCommonAncestor(node, node3, node5)
print(ancestor.val)

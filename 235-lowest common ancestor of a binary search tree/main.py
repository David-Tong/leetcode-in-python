class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if (root.val - p.val) * (root.val - q.val) <= 0:
            return root
        return self.lowestCommonAncestor(root.left if root.val > p.val else root.right, p, q)

node = TreeNode(6)
node2 = TreeNode(2)
node3 = TreeNode(8)
node4 = TreeNode(0)
node5 = TreeNode(4)
node6 = TreeNode(7)
node7 = TreeNode(9)
node8 = TreeNode(3)
node9 = TreeNode(5)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node5.left = node8
node5.right = node9

p = node2
q = node5

solution = Solution()
ancestor = solution.lowestCommonAncestor(node, p, q)
print(ancestor.val)

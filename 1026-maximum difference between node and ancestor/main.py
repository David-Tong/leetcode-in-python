class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def findMaxDiff(node, maxi, mini):
            self.ans = max(self.ans, max(abs(maxi - node.val), abs(mini - node.val)))
            maxi = max(maxi, node.val)
            mini = min(mini, node.val)

            if node.left:
                findMaxDiff(node.left, maxi, mini)

            if node.right:
                findMaxDiff(node.right, maxi, mini)

        findMaxDiff(root, root.val, root.val)
        return self.ans


node = TreeNode(8)
node2 = TreeNode(3)
node3 = TreeNode(10)
node4 = TreeNode(1)
node5 = TreeNode(6)
node6 = TreeNode(14)
node7 = TreeNode(4)
node8 = TreeNode(7)
node9 = TreeNode(13)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
node5.left = node7
node5.right = node8
node6.left = node9


node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(0)
node4 = TreeNode(3)

node.right = node2
node2.right = node3
node3.left = node4

solution = Solution()
print(solution.maxAncestorDiff(node))

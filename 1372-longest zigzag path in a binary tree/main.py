# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # left - max zigzag path, previous direction is left
        # right -               , previous direction is right
        def doZigZag(node, left, right):
            self.ans = max(self.ans, max(left, right))
            if node.left:
                doZigZag(node.left, right + 1, 0)
            if node.right:
                doZigZag(node.right, 0, left + 1)

        self.ans = 0
        if root.left:
            doZigZag(root.left, 1, 0)
        if root.right:
            doZigZag(root.right, 0, 1)

        return self.ans


node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)

node.right = node2
node2.left = node3
node2.right = node4
node4.left = node5
node4.right = node6
node5.right = node7
node7.right = node8

"""
node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

node.left = node2
node.right = node3
node2.right = node4
node4.left = node5
node4.right = node6
node5.right = node7
"""
"""
node = TreeNode(1)
"""

node = TreeNode(1)
node2 = TreeNode(2)

node.left = node2

solution = Solution()
print(solution.longestZigZag(node))

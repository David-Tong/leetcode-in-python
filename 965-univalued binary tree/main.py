# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # process
        stack = list()
        def leftMost(node):
            while node:
                stack.append(node)
                node = node.left

        leftMost(root)
        while stack:
            node = stack.pop()
            if node.val != root.val:
                return False
            leftMost(node.right)

        return True


"""
node = TreeNode(1)
node2 = TreeNode(1)
node3 = TreeNode(1)
node4 = TreeNode(1)
node5 = TreeNode(1)
node6 = TreeNode(1)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
"""

node = TreeNode(2)
node2 = TreeNode(2)
node3 = TreeNode(2)
node4 = TreeNode(5)
node5 = TreeNode(2)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5

solution = Solution()
print(solution.isUnivalTree(node))

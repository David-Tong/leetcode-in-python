class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def leftMost(node, stack):
            while node:
                stack.append(node)
                node = node.left

        stack = []
        leftMost(root, stack)
        count = 0
        while stack:
            node = stack.pop()
            count += 1
            if count == k:
                return node.val
            leftMost(node.right, stack)





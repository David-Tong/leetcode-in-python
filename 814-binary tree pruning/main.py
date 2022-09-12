class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def pruneTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def doPrune(node):
            if node.val == 1:
                prune = False
            else:
                prune = True

            if node.left:
                if node.left.val == 1:
                    prune = False
                if doPrune(node.left):
                    node.left = None
                else:
                    prune = False

            if node.right:
                if node.right.val == 1:
                    prune = False
                if doPrune(node.right):
                    node.right = None
                else:
                    prune = False

            return prune

        dummy = TreeNode(0)
        dummy.left = root
        dummy.right = TreeNode(1)
        doPrune(dummy)

        return dummy.left

"""
node = TreeNode(1)
node2 = TreeNode(0)
node3 = TreeNode(0)
node4 = TreeNode(1)

node.right = node2
node2.left = node3
node2.right = node4
"""

"""
node = TreeNode(1)
node2 = TreeNode(0)
node3 = TreeNode(1)
node4 = TreeNode(0)
node5 = TreeNode(0)
node6 = TreeNode(0)
node7 = TreeNode(1)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node5
node3.right = node7
"""

node = TreeNode(1)
node2 = TreeNode(1)
node3 = TreeNode(0)
node4 = TreeNode(1)
node5 = TreeNode(1)
node6 = TreeNode(0)
node7 = TreeNode(1)
node8 = TreeNode(0)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node5
node3.right = node7
node3.left = node8

solution = Solution()
node = solution.pruneTree(node)

node

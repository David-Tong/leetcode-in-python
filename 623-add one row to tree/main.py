class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        def doAdd(node, level, val, depth):
            if node:
                if level + 1 == depth:
                    left = node.left
                    right = node.right
                    added_left = TreeNode(val=val, left=left, right=None)
                    added_right = TreeNode(val=val, left=None, right=right)
                    node.left = added_left
                    node.right = added_right
                else:
                    doAdd(node.left, level + 1, val, depth)
                    doAdd(node.right, level + 1, val, depth)

        if depth == 1:
            new_root = TreeNode(val, left=root, right=None)
            return new_root
        else:
            doAdd(root, 1, val, depth)
            return root


"""
node = TreeNode(4)
node2 = TreeNode(2)
node3 = TreeNode(6)
node4 = TreeNode(3)
node5 = TreeNode(1)
node6 = TreeNode(5)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6

val = 1
depth = 2
"""

node = TreeNode(4)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(1)

node.left = node2
node2.left = node3
node2.right = node4

val = 1
depth = 3
depth = 1
depth = 4

solution = Solution()
node = solution.addOneRow(node, val, depth)

node

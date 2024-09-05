# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        def doRemove(parent, node, isLeft):
            if node is None:
                return True
            left_empty = doRemove(node, node.left, True)
            right_empty = doRemove(node, node.right, False)
            if left_empty and right_empty:
                    if node.val == target:
                        if isLeft:
                            parent.left = None
                        else:
                            parent.right = None
                        # return True when child is None
                        return True
            return False

        dummy = TreeNode(-1)
        dummy.left = root
        doRemove(dummy, root, True)

        return dummy.left


"""
node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(2)
node5 = TreeNode(2)
node6 = TreeNode(4)

node.left = node2
node.right = node3
node2.left = node4
node3.left = node5
node3.right = node6

target = 2
"""

node = TreeNode(1)
node2 = TreeNode(3)
node3 = TreeNode(3)
node4 = TreeNode(3)
node5 = TreeNode(2)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5

target = 3

"""
node = TreeNode(1)
node2 = TreeNode(1)
node3 = TreeNode(1)

node.left = node2
node.right = node3

target = 1
"""

solution = Solution()
root = solution.removeLeafNodes(node, target)

root

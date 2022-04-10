class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def compareTrees(node, node2):
            if node and node2:
                if node.val == node2.val:
                    return compareTrees(node.left, node2.right) & compareTrees(node.right, node2.left)
                else:
                    return False

            if node is None and node2 is None:
                return True
            else:
                return False

        return compareTrees(root, root)

"""
node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(2)
node4 = TreeNode(3)
node5 = TreeNode(4)
node6 = TreeNode(4)
node7 = TreeNode(3)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
"""

node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(2)
node4 = TreeNode(3)
node5 = TreeNode(3)

node.left = node2
#node.right = node3
#node2.right = node4
#node3.right = node5

solution = Solution()
print(solution.isSymmetric(node))

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def doBalance(node):
            if not node:
                return (True, 0)

            left_balanced, left_height = doBalance(node.left)
            right_balanced, right_height = doBalance(node.right)

            if abs(left_height - right_height) <= 1:
                return (left_balanced & right_balanced, max(left_height, right_height) + 1)
            else:
                return (False, max(left_height, right_height) + 1)

        balanced, _ = doBalance(root)
        return balanced


node = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)

node.left = node2
node.right = node3
node3.left = node4
node3.right = node5

solution = Solution()
print(solution.isBalanced(node))

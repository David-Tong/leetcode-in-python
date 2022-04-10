class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def doValid(node):
            MAX_VALUE = float("-inf")
            MIN_VALUE = float("inf")

            if not node:
                return (MAX_VALUE, MIN_VALUE, True)

            maxi_left, mini_left, valid = doValid(node.left)
            if valid:
                if node.val <= maxi_left:
                    return (MAX_VALUE, MIN_VALUE, False)
            else:
                return (MAX_VALUE, MIN_VALUE, False)

            maxi_right, mini_right, valid = doValid(node.right)
            if valid:
                if node.val >= mini_right:
                    return (MAX_VALUE, MIN_VALUE, False)
            else:
                return (MAX_VALUE, MIN_VALUE, False)

            return max(node.val, maxi_right), min(node.val, mini_left), True

        maxi, mini, valid = doValid(root)
        return valid


"""
node = TreeNode(5)
node2 = TreeNode(1)
node3 = TreeNode(6)
node4 = TreeNode(3)
node5 = TreeNode(7)

node.left = node2
node.right = node3
node3.left = node4
node3.right = node5
"""

node = TreeNode(2)
node2 = TreeNode(2)
node3 = TreeNode(2)

node.left = node2
node.right = node3

solution = Solution()
print(solution.isValidBST(node))

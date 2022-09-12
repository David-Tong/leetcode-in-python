class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def doGood(node, maxi):
            if node.val >= maxi:
                maxi = node.val
                self.ans += 1

            if node.left:
                doGood(node.left, maxi)

            if node.right:
                doGood(node.right, maxi)

        doGood(root, float("-inf"))
        return self.ans


"""
node = TreeNode(3)
node2 = TreeNode(1)
node3 = TreeNode(4)
node4 = TreeNode(3)
node5 = TreeNode(1)
node6 = TreeNode(5)

node.left = node2
node.right = node3
node2.left = node4
node3.left = node5
node3.right = node6
"""

"""
node = TreeNode(3)
node2 = TreeNode(3)
node3 = TreeNode(4)
node4 = TreeNode(2)

node.left = node2
node2.left = node3
node2.right = node4
"""

node = TreeNode(1)

solution = Solution()
print(solution.goodNodes(node))

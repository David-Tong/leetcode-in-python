# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def balance(node):
            l, r = 0, 0
            if node.left:
                l = balance(node.left)
            if node.right:
                r = balance(node.right)
            self.ans += abs(l) + abs(r)
            return node.val - 1 + l + r

        balance(root)
        return self.ans


"""
node = TreeNode(3)
node2 = TreeNode(0)
node3 = TreeNode(0)

node.left = node2
node.right = node3
"""

"""
node = TreeNode(0)
node2 = TreeNode(3)
node3 = TreeNode(0)

node.left = node2
node.right = node3
"""

"""
node = TreeNode(1)
node2 = TreeNode(0)
node3 = TreeNode(0)
node4 = TreeNode(3)

node.left = node2
node.right = node3
node2.right = node4
"""

node = TreeNode(0)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(0)
node5 = TreeNode(0)
node6 = TreeNode(1)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node4.left = node6

solution = Solution()
print(solution.distributeCoins(node))

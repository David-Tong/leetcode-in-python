# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: Optional[TreeNode]
        :type limit: int
        :rtype: Optional[TreeNode]
        """
        # process
        # recursion function
        def search(node, total):
            if not node:
                return float("-inf")

            total += node.val
            maxi = max(search(node.left, total), search(node.right, total))
            if maxi == float("-inf"):
                maxi = 0
            node.path = total + maxi
            return maxi + node.val

        def delete(node):
            if node.left:
                delete(node.left)
                if node.left.path < limit:
                    node.left = None
            if node.right:
                delete(node.right)
                if node.right.path < limit:
                    node.right = None

        # dummy node
        dummy = TreeNode(0)
        dummy.left = root

        search(dummy, 0)
        delete(dummy)

        # post-process
        ans = dummy.left
        return ans


"""
node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(-99)
node6 = TreeNode(-99)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)
node10 = TreeNode(-99)
node11 = TreeNode(-99)
node12 = TreeNode(12)
node13 = TreeNode(13)
node14 = TreeNode(-99)
node15 = TreeNode(14)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node4.left = node8
node4.right = node9
node5.left = node10
node5.right = node11
node6.left = node12
node6.right = node13
node7.left = node14
node7.right = node15

limit = 1
"""

"""
node = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(8)
node4 = TreeNode(11)
node5 = TreeNode(17)
node6 = TreeNode(4)
node7 = TreeNode(7)
node8 = TreeNode(1)
node9 = TreeNode(5)
node10 = TreeNode(3)

node.left = node2
node.right = node3
node2.left = node4
node3.left = node5
node3.right = node6
node4.left = node7
node4.right = node8
node6.left = node9
node6.right = node10

limit = 22
"""

node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(-3)
node4 = TreeNode(-5)
node5 = TreeNode(4)

node.left = node2
node.right = node3
node2.left = node4
node3.left = node5

limit = -1

"""
node = TreeNode(10)
node2 = TreeNode(5)
node3 = TreeNode(10)

limit = 21
"""

solution = Solution()
root = solution.sufficientSubset(node, limit)

root

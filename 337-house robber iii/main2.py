class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from functools import lru_cache
        @lru_cache(maxsize=10000)
        def doRob(node, robbed):
            if not node:
                return 0

            amount = 0
            if not robbed:
                amount = max(amount, node.val + doRob(node.left, True) + doRob(node.right, True))
            amount = max(amount, doRob(node.left, False) + doRob(node.right, False))
            return amount

        return doRob(root, False)


node = TreeNode(1)
node2 = TreeNode(4)
node3 = TreeNode(2)
node4 = TreeNode(1)
node5 = TreeNode(7)
node6 = TreeNode(4)
node7 = TreeNode(9)
node8 = TreeNode(11)

node.left = node2
node.right = node3
node2.left = node4
node3.left = node5
node3.right = node6
node6.left = node7
node6.right = node8


solution = Solution()
print(solution.rob(node))

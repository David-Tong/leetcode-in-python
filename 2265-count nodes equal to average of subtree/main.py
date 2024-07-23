# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def doAverage(node):
            if not node:
                return 0, 0
            else:
                left_total, left_nodes = doAverage(node.left)
                right_total, right_nodes = doAverage(node.right)
                total = left_total + right_total + node.val
                nodes = left_nodes + right_nodes + 1
                if node.val == total / nodes:
                    self.ans += 1

                return total, nodes

        self.ans = 0
        doAverage(root)

        return self.ans


"""
node = TreeNode(4)
node2 = TreeNode(8)
node3 = TreeNode(5)
node4 = TreeNode(0)
node5 = TreeNode(1)
node6 = TreeNode(6)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
"""

node = TreeNode(1)
node = None

solution = Solution()
print(solution.averageOfSubtree(node))

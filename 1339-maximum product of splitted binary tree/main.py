class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        MODULA = 10 ** 9 + 7

        self.totals = list()
        def getSum(node):
            total = node.val

            if node.left:
                total += getSum(node.left)

            if node.right:
                total += getSum(node.right)

            self.totals.append(total)
            return total

        sumi = getSum(root)

        ans = 0
        for total in self.totals:
            ans = max(ans, total * (sumi - total))
        return ans % MODULA


"""
node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
"""

node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node.right = node2
node2.left = node3
node2.right = node4
node4.left = node5
node4.right = node6

solution = Solution()
print(solution.maxProduct(node))

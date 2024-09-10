class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = list()

        def leftMost(node):
            while node:
                stack.append(node)
                node = node.left

        leftMost(root)
        prev = float("-inf")
        ans = float("inf")
        while stack:
            node = stack.pop()
            ans = min(ans, node.val - prev)
            prev = node.val
            leftMost(node.right)
        return ans


node = TreeNode(4)
node2 = TreeNode(2)
node3 = TreeNode(6)
node4 = TreeNode(1)
node5 = TreeNode(3)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5

node = TreeNode(1)
node2 = TreeNode(0)
node3 = TreeNode(48)
node4 = TreeNode(12)
node5 = TreeNode(49)

node.left = node2
node.right = node3
node3.left = node4
node3.right = node5

solution = Solution()
print(solution.getMinimumDifference(node))

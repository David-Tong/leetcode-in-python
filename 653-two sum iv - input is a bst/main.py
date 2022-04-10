class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def leftMost(stack, node):
            while node:
                stack.append(node)
                node = node.left

        visited = set()
        stack = []
        leftMost(stack, root)
        while len(stack) > 0:
            curr = stack.pop(-1)
            if k - curr.val in visited:
                return True
            visited.add(curr.val)
            leftMost(stack, curr.right)
        return False


node = TreeNode(1)
node2 = TreeNode(3)
node3 = TreeNode(6)
node4 = TreeNode(2)
node5 = TreeNode(4)
node6 = TreeNode(7)


node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.right = node6


k = 28
solution = Solution()
print(solution.findTarget(node, k))

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # pre-process
        # pre-order traversal
        def mostLeft(node):
            while node:
                stack.append(node)
                node = node.left

        stack = list()
        mostLeft(root)
        numbers = set()
        while stack:
            node = stack.pop()
            if node.val not in numbers:
                numbers.add(node.val)
            mostLeft(node.right)

        # proces
        numbers = sorted(list(numbers))
        if len(numbers) < 2:
            return -1
        else:
            return numbers[1]


"""
node = TreeNode(2)
node2 = TreeNode(2)
node3 = TreeNode(5)
node4 = TreeNode(5)
node5 = TreeNode(7)

node.left = node2
node.right = node3
node3.left = node4
node3.right = node5
"""

"""
node = TreeNode(2)
node2 = TreeNode(2)
node3 = TreeNode(2)

node.left = node2
node.right = node3
"""

node = TreeNode(5)
node2 = TreeNode(8)
node3 = TreeNode(5)

node.left = node2
node.right = node3

solution = Solution()
print(solution.findSecondMinimumValue(node))

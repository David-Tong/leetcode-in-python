class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        def leftMost(node, stack):
            while node:
                stack.append(node)
                node = node.left

        stack = list()
        stack2 = list()
        leftMost(original, stack)
        leftMost(cloned, stack2)
        while stack:
            node = stack.pop()
            node2 = stack2.pop()
            if node == target:
                return node2
            leftMost(node.right, stack)
            leftMost(node2.right, stack2)
        return None


node11 = TreeNode(7)
node12 = TreeNode(4)
node13 = TreeNode(3)
node14 = TreeNode(6)
node15 = TreeNode(19)

node11.left = node12
node11.right = node13
node13.left = node14
node13.right = node15

node21 = TreeNode(7)
node22 = TreeNode(4)
node23 = TreeNode(3)
node24 = TreeNode(6)
node25 = TreeNode(19)

node21.left = node22
node21.right = node23
node23.left = node24
node23.right = node25

"""
node11 = TreeNode(1)
node12 = TreeNode(2)
node13 = TreeNode(3)
node14 = TreeNode(4)
node15 = TreeNode(5)
node16 = TreeNode(6)
node17 = TreeNode(7)
node18 = TreeNode(8)
node19 = TreeNode(9)
node110 = TreeNode(10)

node11.left = node12
node11.right = node13
node12.left = node14
node12.right = node15
node13.left = node16
node13.right = node17
node14.left = node18
node14.right = node19
node15.left = node110

node21 = TreeNode(1)
node22 = TreeNode(2)
node23 = TreeNode(3)
node24 = TreeNode(4)
node25 = TreeNode(5)
node26 = TreeNode(6)
node27 = TreeNode(7)
node28 = TreeNode(8)
node29 = TreeNode(9)
node210 = TreeNode(10)

node21.left = node22
node21.right = node23
node22.left = node24
node22.right = node25
node23.left = node26
node23.right = node27
node24.left = node28
node24.right = node29
node25.left = node210
"""

solution = Solution()
node = solution.getTargetCopy(node11, node21, node13)

print(node.val)

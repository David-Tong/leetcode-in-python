class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        def leftMost(node, stack):
            while node:
                stack.append(node)
                node = node.left

        output = []
        stack1 = []
        stack2 = []

        leftMost(root1, stack1)
        leftMost(root2, stack2)
        while len(stack1) > 0 and len(stack2) > 0:
            if stack1[-1].val <= stack2[-1].val:
                node = stack1.pop()
                output.append(node.val)
                leftMost(node.right, stack1)
            else:
                node = stack2.pop()
                output.append(node.val)
                leftMost(node.right, stack2)

        while len(stack1) > 0:
            node = stack1.pop()
            output.append(node.val)
            leftMost(node.right, stack1)

        while len(stack2) > 0:
            node = stack2.pop()
            output.append(node.val)
            leftMost(node.right, stack2)

        return output


node21 = TreeNode(5)
node22 = TreeNode(1)
node23 = TreeNode(7)
node24 = TreeNode(0)
node25 = TreeNode(2)
node21.left = node22
node21.right = node23
node22.left = node24
node22.right = node25

solution = Solution()
print(solution.getAllElements(None, node21))

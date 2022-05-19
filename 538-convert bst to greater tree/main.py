class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def leftMost(node, stack):
            while node:
                stack.append(node)
                node = node.left

        if not root:
            return None

        stack = []
        leftMost(root, stack)
        # calculate the total
        total = 0
        while stack:
            node = stack.pop()
            total += node.val
            if node.right:
                leftMost(node.right, stack)

        stack = []
        leftMost(root, stack)
        # update node value, build greater tree, by total - prefix
        prefix = 0
        while stack:
            node = stack.pop()
            tmp = node.val
            node.val = total - prefix
            prefix += tmp
            if node.right:
                leftMost(node.right, stack)

        return root


node = TreeNode(4)
node2 = TreeNode(1)
node3 = TreeNode(6)
node4 = TreeNode(0)
node5 = TreeNode(2)
node6 = TreeNode(5)
node7 = TreeNode(7)
node8 = TreeNode(3)
node9 = TreeNode(8)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node5.right = node8
node7.right = node9


solution = Solution()
print(solution.convertBST(node))

node
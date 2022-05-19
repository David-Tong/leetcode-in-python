class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def leftMost(node, stack):
            while node:
                stack.append(node)
                node = node.left

        head = None
        prev = None
        stack = []
        leftMost(root, stack)
        while stack:
            node = stack.pop()
            leftMost(node.right, stack)
            if prev:
                prev.right = node
                prev.left = None
                prev = node
            else:
                head = node
                prev = node

        node.left = None
        node.right = None

        return head


node = TreeNode(5)
node2 = TreeNode(3)
node3 = TreeNode(6)
node4 = TreeNode(2)
node5 = TreeNode(4)
node6 = TreeNode(8)
node9 = TreeNode(1)
node10 = TreeNode(7)
node11 = TreeNode(9)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
node4.left = node9
node6.left = node10
node6.right = node11

solution = Solution()
print(solution.increasingBST(node))
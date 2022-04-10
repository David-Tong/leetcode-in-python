class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def leftMost(node, stack):
            while node:
                stack.append(node)
                node = node.left

        stack = []
        mono_stack = []
        leftMost(root, stack)
        first = None
        second = None
        while len(stack) > 0:
            node = stack.pop()
            if node.right:
                leftMost(node.right, stack)

            if not first:
                while len(mono_stack) > 0 and mono_stack[-1].val > node.val:
                    first = mono_stack.pop()
                second = node
                mono_stack.append(node)
            else:
                if len(mono_stack) > 0 and mono_stack[-1].val > node.val:
                    second = node
                    break

        tmp = first.val
        first.val = second.val
        second.val = tmp


node = TreeNode(1)
node2 = TreeNode(3)
node3 = TreeNode(2)
node.left = node2
node2.right = node3

solution = Solution()
solution.recoverTree(node)

print(node)

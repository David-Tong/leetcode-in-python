class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return []

        # pre-order traversal
        stack = []
        stack.append(root)

        prev = None
        while stack:
            curr = stack.pop()
            if prev:
                prev.left = None
                prev.right = curr
            prev = curr

            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

        return root


node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(5)
node4 = TreeNode(3)
node5 = TreeNode(4)
node6 = TreeNode(6)

#node.left = node2
#node.right = node3
node2.left = node4
node2.right = node5
node5.right = node6

solution = Solution()
node = solution.flatten(node)

while node:
    print(node.val)
    node = node.right
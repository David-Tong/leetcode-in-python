class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 1

        def doLongest(node):
            longest = 1

            if node.left:
                left_longest = doLongest(node.left)
                if node.left.val != node.val:
                    left_longest = 0
                self.ans = max(self.ans, left_longest + 1)
                longest = max(longest, left_longest + 1)

            right_longest = 0
            if node.right:
                right_longest = doLongest(node.right)
                if node.right.val != node.val:
                    right_longest = 0
                self.ans = max(self.ans, right_longest + 1)
                longest = max(longest, right_longest + 1)

            if node.left and node.right and node.left.val == node.right.val == node.val:
                self.ans = max(self.ans, left_longest + right_longest + 1)

            return longest

        if root:
            doLongest(root)
            return self.ans - 1

        return 0


"""
node = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(5)
node4 = TreeNode(1)
node5 = TreeNode(1)
node6 = TreeNode(5)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
"""

node = TreeNode(1)
node2 = TreeNode(4)
node3 = TreeNode(5)
node4 = TreeNode(4)
node5 = TreeNode(4)
node6 = TreeNode(5)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.right = node6

#node = None

solution = Solution()
print(solution.longestUnivaluePath(node))

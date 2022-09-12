class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # return 0 - None, 1 - Covered, 2 - Camera
        def doCover(node):
            if node is None:
                return 1

            left_status = doCover(node.left)
            right_status = doCover(node.right)

            if left_status == 0 or right_status == 0:
                self.ans += 1
                return 2

            if left_status == 2 or right_status == 2:
                return 1

            return 0

        self.ans = 0
        if doCover(root) == 0:
            self.ans += 1

        return self.ans


node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)

node.left = node2
node2.left = node3
node2.right = node4

"""
node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node.left = node2
node2.left = node3
node3.left = node4
node4.right = node5
"""

"""
node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node.left = node2
node2.right = node3
node3.left = node4
node4.right = node5
node5.left = node6
"""

node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)

node.right = node2
node2.right = node3
node3.right = node4


solution = Solution()
print(solution.minCameraCover(node))

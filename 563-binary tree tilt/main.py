class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def doTilt(node):
            if node.left:
                left = doTilt(node.left)
            else:
                left = (0, 0)

            if node.right:
                right = doTilt(node.right)
            else:
                right = (0, 0)

            # (tilt, sum)
            tilt = left[0] + right[0] + abs(left[1] - right[1])
            sum = node.val + left[1] + right[1]
            print(node.val, tilt, sum)
            return (tilt, sum)

        if root:
            ans = doTilt(root)
            return ans[0]

        else:
            return 0


"""
node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node.left = node2
node.right = node3
"""

"""
node = TreeNode(4)
node2 = TreeNode(2)
node3 = TreeNode(9)
node4 = TreeNode(3)
node5 = TreeNode(5)
node6 = TreeNode(7)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
"""

node = TreeNode(21)
node2 = TreeNode(7)
node3 = TreeNode(14)
node4 = TreeNode(1)
node5 = TreeNode(1)
node6 = TreeNode(2)
node7 = TreeNode(2)
node8 = TreeNode(3)
node9 = TreeNode(3)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node4.left = node8
node4.right = node9

node = None

solution = Solution()
print(solution.findTilt(node))
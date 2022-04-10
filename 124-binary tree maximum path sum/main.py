class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        import sys
        def doMaxPathSum(root):
            if root is None:
                return 0
            else:
                left_sum = max(0, doMaxPathSum(root.left))
                right_sum = max(0, doMaxPathSum(root.right))
                self.ans = max(self.ans, left_sum + right_sum + root.val)
                max_sum = max(left_sum, right_sum) + root.val
                return max_sum

        self.ans = -1001
        doMaxPathSum(root)
        return self.ans


node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node.left = node2
node.right = node3

node = TreeNode(-10)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)
node.left = node2
node.right = node3
node3.left = node4
node3.right = node5

#node = TreeNode(-2)
#node2 = TreeNode(1)
#node.left = node2

solution = Solution()
print(solution.maxPathSum(node))



class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def doPathSum(node, pathSum, targetSum):
            ans = False
            if node.left is None and node.right is None:
                if pathSum + node.val == targetSum:
                    ans = True
            if node.left:
                ans = ans | doPathSum(node.left, pathSum + node.val, targetSum)

            if node.right:
                ans = ans | doPathSum(node.right, pathSum + node.val, targetSum)
            return ans

        if root is None:
            return False
        return doPathSum(root, 0, targetSum)


node = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(8)
node4 = TreeNode(11)
node5 = TreeNode(13)
node6 = TreeNode(4)
node7 = TreeNode(7)
node8 = TreeNode(2)
node9 = TreeNode(1)

#node.left = node2
#node.right = node3
node2.left = node4
node3.left = node5
node3.right = node6
node4.left = node7
node4.right = node8
node6.right = node9

targetSum = 5

solution = Solution()
print(solution.hasPathSum(node, targetSum))

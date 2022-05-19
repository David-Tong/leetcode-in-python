class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        self.anses = []

        def doSum(node, path, targetSum):
            path.append(node.val)
            if not node.left and not node.right:
                if sum(path) == targetSum:
                    self.anses.append(path[:])

            if node.left:
                doSum(node.left, path[:], targetSum)
            if node.right:
                doSum(node.right, path[:], targetSum)

        if not root:
            return []

        doSum(root, [], targetSum)
        return self.anses


node = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(8)
node4 = TreeNode(11)
node5 = TreeNode(13)
node6 = TreeNode(4)
node7 = TreeNode(7)
node8 = TreeNode(2)
node9 = TreeNode(5)
node10 = TreeNode(1)

node.left = node2
node.right = node3
#node2.left = node4
#node3.left = node5
#node3.right = node6
node4.left = node7
node4.right = node8
node6.left = node9
node6.right = node10

targetSum = 22
targetSum = 17

solution = Solution()
print(solution.pathSum(node, targetSum))

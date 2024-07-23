# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def doEvaluate(node):
            if node.val == 0:
                return False
            elif node.val == 1:
                return True
            elif node.val == 2:
                return doEvaluate(node.left) | doEvaluate(node.right)
            elif node.val == 3:
                return doEvaluate(node.left) & doEvaluate(node.right)
        return doEvaluate(root)


node = TreeNode(2)
node2 = TreeNode(1)
node3 = TreeNode(3)
node4 = TreeNode(0)
node5 = TreeNode(1)

node.left = node2
node.right = node3
node3.left = node4
node3.right = node5

solution = Solution()
print(solution.evaluateTree(node))

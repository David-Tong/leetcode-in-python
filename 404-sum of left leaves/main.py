class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def doSum(node, left):
            sumi = 0
            if node:
                if not node.left and not node.right:
                    if left:
                        sumi += node.val
                if node.left:
                    sumi += doSum(node.left, True)
                if node.right:
                    sumi += doSum(node.right, False)
            return sumi

        return doSum(root, False)


node = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)
node6 = TreeNode(11)
node7 = TreeNode(25)

node.left = node2
node.right = node3
node3.left = node4
node3.right = node5
node2.left = node6
node4.right = node7

solution = Solution()
print(solution.sumOfLeftLeaves(node))

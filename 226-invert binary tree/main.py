class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def doInvert(node):
            if node:
                tmp = node.left
                node.left = node.right
                node.right = tmp
                if node.left:
                    doInvert(node.left)
                if node.right:
                    doInvert(node.right)
        doInvert(root)
        return root


node = TreeNode(4)
node2 = TreeNode(2)
node3 = TreeNode(7)
node4 = TreeNode(1)
node5 = TreeNode(3)
node6 = TreeNode(6)
node7 = TreeNode(9)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

solution = Solution()
root = solution.invertTree(node)

print(root)


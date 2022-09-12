class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getDepth(node):
            if node.left:
                ld = getDepth(node.left)
            if node.right:
                rd = getDepth(node.right)

            if node.left:
                if node.right:
                    return min(ld, rd) + 1
                else:
                    return ld + 1
            else:
                if node.right:
                    return rd + 1
                else:
                    return 1
        if root:
            return getDepth(root)
        else:
            return 0


node = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)

node.left = node2
node.right = node3
node3.left = node4
node4.right = node5

node = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(4)
node4 = TreeNode(5)
node5 = TreeNode(6)

node.right = node2
node2.right = node3
node3.right = node4
node4.right = node5

solution = Solution()
print(solution.minDepth(node))

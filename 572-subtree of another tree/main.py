class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        def doSubtree(root, subRoot):
            if root and subRoot:
                if root.val == subRoot.val:
                    return doSubtree(root.left, subRoot.left) & doSubtree(root.right, subRoot.right)
                else:
                    return False
            elif not root and not subRoot:
                return True
            else:
                return False

        if doSubtree(root, subRoot):
            return True
        else:
            if root.left and self.isSubtree(root.left, subRoot):
                return True
            if root.right and self.isSubtree(root.right, subRoot):
                return True
        return False


node11 = TreeNode(3)
node12 = TreeNode(4)
node13 = TreeNode(5)
node14 = TreeNode(1)
node15 = TreeNode(2)
node16 = TreeNode(0)

node21 = TreeNode(4)
node22 = TreeNode(1)
node23 = TreeNode(2)

node11.left = node12
node11.right = node13
node12.left = node14
node12.right = node15
node15.left = node16

node21.left = node22
node21.right = node23

solution = Solution()
print(solution.isSubtree(node11, node21))

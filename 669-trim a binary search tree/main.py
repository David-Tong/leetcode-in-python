class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        if not root:
            return root

        if root.val < low:
            return self.trimBST(root.right, low, high)
        elif root.val > high:
            return self.trimBST(root.left, low, high)
        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root


node = TreeNode(3)
node2 = TreeNode(0)
node3 = TreeNode(4)
node4 = TreeNode(2)
node5 = TreeNode(1)

node.left = node2
node.right = node3
node2.right = node4
node4.left = node5

low = 1
high = 3

solution = Solution()
print(solution.trimBST(node, low, high))

node
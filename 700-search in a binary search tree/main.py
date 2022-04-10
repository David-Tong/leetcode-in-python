class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def doSearch(node, val):
            if node is None:
                return None
            if val == node.val:
                return node
            elif val < node.val:
                return doSearch(node.left, val)
            else:
                return doSearch(node.right, val)
        return doSearch(root, val)


node = TreeNode(4)
node2 = TreeNode(2)
node3 = TreeNode(7)
node4 = TreeNode(1)
node5 = TreeNode(3)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5

val = 2

solution = Solution()
root = solution.searchBST(node, val)

print(root.val)



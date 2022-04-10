class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def doInsert(parent, node, val, is_left):
            if node is None:
                new = TreeNode(val)
                if is_left:
                    parent.left = new
                else:
                    parent.right = new
            else:
                if val < node.val:
                    doInsert(node, node.left, val, True)
                else:
                    doInsert(node, node.right, val, False)

        if root is None:
            return TreeNode(val)

        doInsert(None, root, val, None)
        return root


node = TreeNode(40)
node2 = TreeNode(20)
node3 = TreeNode(60)
node4 = TreeNode(10)
node5 = TreeNode(30)
node6 = TreeNode(50)
node7 = TreeNode(70)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

root = None
val = 25

solution = Solution()
root = solution.insertIntoBST(node, val)

print(root.val)



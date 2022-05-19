class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def successor(self, node):
        node = node.right
        while node.left:
            node = node.left
        return node.val

    def predecessor(self, node):
        node = node.left
        while node.right:
            node = node.right
        return node.val

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # leaf node
            if not root.left and not root.right:
                root = None
            # with right tree
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # with left tree
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        return root


"""
node = TreeNode(5)
node2 = TreeNode(3)
node3 = TreeNode(6)
node4 = TreeNode(2)
node5 = TreeNode(4)
node6 = TreeNode(7)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.right = node6

key = 3
key = 11
key = 5
key = 7
"""

node = TreeNode(50)
node2 = TreeNode(30)
node3 = TreeNode(70)
node4 = TreeNode(40)
node5 = TreeNode(60)
node6 = TreeNode(80)

node.left = node2
node.right = node3
node2.right = node4
node3.left = node5
node3.right = node6

key = 50

solution = Solution()
node = solution.deleteNode(node, key)

node
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        def doMerge(node1, node2, parent, is_left):
            if node1:
                if node2:
                    node = TreeNode(node1.val + node2.val)
                else:
                    node = TreeNode(node1.val)
            else:
                if node2:
                    node = TreeNode(node2.val)
                else:
                    return

            if parent:
                if is_left:
                    parent.left = node
                else:
                    parent.right = node

            node1_left = None
            node1_right = None
            node2_left = None
            node2_right = None
            if node1:
                node1_left = node1.left
                node1_right = node1.right

            if node2:
                node2_left = node2.left
                node2_right = node2.right

            doMerge(node1_left, node2_left, node, True)
            doMerge(node1_right, node2_right, node, False)

            if parent is None:
                return node

        return doMerge(root1, root2, None, False)


node11 = TreeNode(1)
node12 = TreeNode(3)
node13 = TreeNode(2)
node14 = TreeNode(5)

node11.left = node12
node11.right = node13
node12.left = node14

node21 = TreeNode(2)
node22 = TreeNode(1)
node23 = TreeNode(3)
node24 = TreeNode(4)
node25 = TreeNode(7)

node21.left = node22
node21.right = node23
node22.right = node24
node23.right = node25

solution = Solution()
root = solution.mergeTrees(node11, node21)

def inOrder(root):
    if root is None:
        return

    inOrder(root.left)
    print(root.val)
    inOrder(root.right)

inOrder(root)
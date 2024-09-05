# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # (include, exclude) - include - the longest path between 2 nodes can be continued
        #                    - exclude -                                  can't
        def doDiameter(node):
            if node.left is None and node.right is None:
                if node == root:
                    return 0, 0
                else:
                    return 1, 1

            include = 0
            exclude = 0
            if node.left:
                include_left, exclude_left = doDiameter(node.left)
                include = max(include, include_left)
                exclude = max(exclude, exclude_left)
            if node.right:
                include_right, exclude_right = doDiameter(node.right)
                include = max(include, include_right)
                exclude = max(exclude, exclude_right)
            if node.left and node.right:
                exclude = max(exclude, include_left + include_right)
            if node == root:
                return include, exclude
            else:
                return include + 1, exclude

        include, exclude = doDiameter(root)
        return max(include, exclude)


"""
node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
"""

"""
node = TreeNode(1)
node2 = TreeNode(2)

node.left = node2
"""

"""
node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)
node10 = TreeNode(10)

node.left = node2
node.right = node3
node2.left = node4
node3.left = node5
node3.right = node6
node5.left = node7
node6.right = node8
node7.left = node9
node9.left = node10
"""

node = TreeNode(1)

solution = Solution()
print(solution.diameterOfBinaryTree(node))

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def doFlipEquiv(node1, node2):
            equiv = False
            if node1 and node2 and node1.val == node2.val:
                if doFlipEquiv(node1.left, node2.left) and doFlipEquiv(node1.right, node2.right):
                    equiv = True
                elif doFlipEquiv(node1.left, node2.right) and doFlipEquiv(node1.right, node2.left):
                    equiv = True
                # print(node1.val, node2.val, equiv)
            elif not node1 and not node2:
                equiv = True
            return equiv
        return doFlipEquiv(root1, root2)


"""
node11 = TreeNode(1)
node12 = TreeNode(2)
node13 = TreeNode(3)
node14 = TreeNode(4)
node15 = TreeNode(5)
node16 = TreeNode(6)
node17 = TreeNode(7)
node18 = TreeNode(8)

node11.left = node12
node11.right = node13
node12.left = node14
node12.right = node15
node13.left = node16
node15.left = node17
node15.right = node18

node21 = TreeNode(1)
node22 = TreeNode(3)
node23 = TreeNode(2)
node24 = TreeNode(6)
node25 = TreeNode(4)
node26 = TreeNode(5)
node27 = TreeNode(8)
node28 = TreeNode(7)

node21.left = node22
node21.right = node23
node22.right = node24
node23.left = node25
node23.right = node26
node26.left = node27
node26.right = node28
"""

"""
node11 = TreeNode(1)
node12 = TreeNode(2)
node13 = TreeNode(3)
node14 = TreeNode(4)
node15 = TreeNode(5)
node16 = TreeNode(6)
node17 = TreeNode(7)
node18 = TreeNode(8)

node11.left = node12
node11.right = node13
node12.left = node14
node12.right = node15
node13.left = node16
node15.left = node17
node15.right = node18

node21 = TreeNode(1)
node22 = TreeNode(3)
node23 = TreeNode(2)
node24 = TreeNode(6)
node25 = TreeNode(4)
node26 = TreeNode(5)
node27 = TreeNode(8)
node28 = TreeNode(7)

node21.left = node22
node21.right = node23
node22.right = node24
node23.left = node25
node23.right = node26
node25.left = node27
node26.right = node28
"""

"""
node11 = None
node21 = None
"""

node11 = None
node21 = TreeNode(1)

solution = Solution()
print(solution.flipEquiv(node11, node21))

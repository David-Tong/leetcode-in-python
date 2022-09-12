class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        self.traversals = defaultdict(lambda: defaultdict(list))

        def doTraversal(node, row, column):
            self.traversals[column][row].append(node.val)
            if node.left:
                doTraversal(node.left, row + 1, column - 1)
            if node.right:
                doTraversal(node.right, row + 1, column + 1)

        doTraversal(root, 0, 0)

        anses = list()
        for column in sorted(self.traversals.keys()):
            ans = list()
            for rows in sorted(self.traversals[column]):
                ans.extend(sorted(self.traversals[column][rows]))
            anses.append(ans)
        return anses


"""
node = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)

node.left = node2
node.right = node3
node3.left = node4
node3.right = node5
"""

"""
node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
"""

node = TreeNode(3)
node2 = TreeNode(1)
node3 = TreeNode(4)
node4 = TreeNode(0)
node5 = TreeNode(2)
node6 = TreeNode(2)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6

solution = Solution()
print(solution.verticalTraversal(node))

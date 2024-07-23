# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # pre-process
        from collections import defaultdict
        sums = defaultdict(int)

        def doSum(node):
            if not node:
                return 0

            sums[node] = node.val + doSum(node.left) + doSum(node.right)
            return sums[node]

        def doGst(node, pval):
            # dfs
            if node.left:
                doGst(node.left, pval)
            if node.right:
                if node.left:
                    doGst(node.right, pval - node.val - sums[node.left])
                else:
                    doGst(node.right, pval - node.val)

            # update
            if node.left:
                node.val = pval - sums[node.left]
            else:
                node.val = pval

        doSum(root)
        doGst(root, sums[root])
        return root


"""
node = TreeNode(4)
node2 = TreeNode(1)
node3 = TreeNode(6)
node4 = TreeNode(0)
node5 = TreeNode(2)
node6 = TreeNode(5)
node7 = TreeNode(7)
node8 = TreeNode(3)
node9 = TreeNode(8)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node5.right = node8
node7.right = node9
"""

node = TreeNode(0)
node2 = TreeNode(1)

node.right = node2

solution = Solution()
print(solution.bstToGst(node))

node

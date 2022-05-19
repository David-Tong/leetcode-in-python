class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        self.ans = 0

        def doSum(node, targetSum, totals):
            print(totals)
            if not node:
                return

            for total in totals + [0]:
                if targetSum - node.val == total:
                    self.ans += 1

            for idx, total in enumerate(totals):
                totals[idx] = total + node.val
            totals.append(node.val)

            doSum(node.left, targetSum, totals[:])
            doSum(node.right, targetSum, totals[:])

        doSum(root, targetSum, [])
        return self.ans


"""
node = TreeNode(10)
node2 = TreeNode(5)
node3 = TreeNode(-3)
node4 = TreeNode(3)
node5 = TreeNode(2)
node6 = TreeNode(11)
node7 = TreeNode(3)
node8 = TreeNode(-2)
node9 = TreeNode(1)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
node4.left = node7
node4.right = node8
node5.right = node9

targetSum = 8
"""

node = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(8)
node4 = TreeNode(11)
node5 = TreeNode(13)
node6 = TreeNode(4)
node7 = TreeNode(7)
node8 = TreeNode(2)
node9 = TreeNode(5)
node10 = TreeNode(1)

node.left = node2
node.right = node3
node2.left = node4
node3.left = node5
node3.right = node6
node4.left = node7
node4.right = node8
node6.left = node9
node6.right = node10

targetSum = 22

solution = Solution()
print(solution.pathSum(node, targetSum))

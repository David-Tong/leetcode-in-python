# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        # pre-process
        self.startValues = list()
        self.startPaths = list()
        self.destValues = list()
        self.destPaths = list()

        def doDriections(node, direction, values, paths):
            if node.val == startValue:
                self.startValues = values + [node.val]
                self.startPaths = paths + [direction]
            elif node.val == destValue:
                self.destValues = values + [node.val]
                self.destPaths = paths + [direction]

            if self.startPaths and self.destPaths:
                pass
            else:
                if node.left:
                    doDriections(node.left, "L", values + [node.val], paths + [direction])
                if node.right:
                    doDriections(node.right, "R", values + [node.val], paths + [direction])

        doDriections(root, "E", list(), list())

        # process
        idx = 0
        M = len(self.startValues)
        N = len(self.destValues)
        while idx < M and idx < N:
            if self.startValues[idx] != self.destValues[idx]:
                break
            idx += 1

        ans = "U" * (M - idx) + "".join(self.destPaths[idx:])
        return ans


"""
node = TreeNode(5)
node2 = TreeNode(1)
node3 = TreeNode(2)
node4 = TreeNode(3)
node5 = TreeNode(6)
node6 = TreeNode(4)

node.left = node2
node.right = node3
node2.left = node4
node3.left = node5
node3.right = node6

startValue = 3
destValue = 6

startValue = 2
destValue = 4

startValue = 6
destValue = 4

startValue = 5
destValue = 4
"""

node = TreeNode(2)
node2 = TreeNode(1)

node.left = node2

startValue = 2
destValue = 1

solution = Solution()
print(solution.getDirections(node, startValue, destValue))

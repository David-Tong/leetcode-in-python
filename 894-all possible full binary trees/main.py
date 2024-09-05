# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n % 2 == 0:
            return list()
        if n == 1:
            return [TreeNode()]

        ans = list()
        for x in range(1, n, 2):
            for l in self.allPossibleFBT(x):
                for r in self.allPossibleFBT(n - 1 - x):
                    root = TreeNode()
                    root.left = l
                    root.right = r
                    ans.append(root)
        return ans


n = 7
n = 3

solution = Solution()
ans = solution.allPossibleFBT(n)

ans

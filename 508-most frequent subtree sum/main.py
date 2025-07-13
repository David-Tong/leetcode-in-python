# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # pre-process
        from collections import defaultdict
        self.totals = defaultdict(int)

        def doSum(node):
            if not node:
                return 0
            else:
                total = node.val + doSum(node.left) + doSum(node.right)
                self.totals[total] += 1
                return total

        # process
        doSum(root)
        maxi_count = max(self.totals.values())
        ans = list()
        for key in self.totals:
            if self.totals[key] == maxi_count:
                ans.append(key)
        return ans


"""
node = TreeNode(5)
node2 = TreeNode(2)
node3 = TreeNode(-3)

node.left = node2
node.right = node3
"""

node = TreeNode(5)
node2 = TreeNode(2)
node3 = TreeNode(-5)

node.left = node2
node.right = node3

solution = Solution()
print(solution.findFrequentTreeSum(node))

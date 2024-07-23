# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def leftMost(node):
            while node:
                stack.append(node)
                node = node.left

        numbers = list()
        stack = list()
        leftMost(root)
        while stack:
            node = stack.pop()
            numbers.append(node.val)
            leftMost(node.right)

        from collections import defaultdict
        dicts = defaultdict(int)

        maxi = 0
        for num in numbers:
            dicts[num] += 1
            maxi = max(maxi, dicts[num])

        ans = list()
        for num in dicts:
            if dicts[num] == maxi:
                ans.append(num)
        return ans


"""
node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(2)

node.right = node2
node2.left = node3
"""

node = TreeNode(0)

solution = Solution()
print(solution.findMode(node))

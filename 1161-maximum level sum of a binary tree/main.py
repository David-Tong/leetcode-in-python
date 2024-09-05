# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque
        bfs = deque()
        bfs.append(root)

        maxi = float("-inf")
        ans = 0
        level = 0
        while bfs:
            level += 1
            total = 0
            size = len(bfs)
            for x in range(size):
                curr = bfs.popleft()
                total += curr.val
                if curr.left:
                    bfs.append(curr.left)
                if curr.right:
                    bfs.append(curr.right)
            if total > maxi:
                maxi = total
                ans = level
        return ans


"""
node = TreeNode(1)
node2 = TreeNode(7)
node3 = TreeNode(0)
node4 = TreeNode(7)
node5 = TreeNode(-8)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
"""

node = TreeNode(989)
node2 = TreeNode(10250)
node3 = TreeNode(98693)
node4 = TreeNode(-89388)
node5 = TreeNode(-32127)

node.right = node2
node2.left = node3
node2.right = node4
node4.right = node5

solution = Solution()
print(solution.maxLevelSum(node))

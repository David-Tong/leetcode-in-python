# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def kthLargestLevelSum(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        # bfs
        from collections import deque
        bfs = deque()
        bfs.append(root)

        # process
        totals = list()
        while bfs:
            L = len(bfs)
            total = 0
            for _ in range(L):
                node = bfs.popleft()
                total += node.val
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
            totals.append(total)

        # post-process
        totals = sorted(totals, reverse=True)
        return totals[k - 1] if k <= len(totals) else -1


"""
node = TreeNode(5)
node2 = TreeNode(8)
node3 = TreeNode(9)
node4 = TreeNode(2)
node5 = TreeNode(1)
node6 = TreeNode(3)
node7 = TreeNode(7)
node8 = TreeNode(4)
node9 = TreeNode(6)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node4.left = node8
node4.right =node9

k = 5
"""

node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node.left = node2
node2.left = node3

k = 3

solution = Solution()
print(solution.kthLargestLevelSum(node, k))
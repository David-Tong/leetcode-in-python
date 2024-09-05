# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import deque
        bfs = deque()
        if root:
            bfs.append(root)

        ans = list()
        while bfs:
            size = len(bfs)
            maxi = float("-inf")
            for _ in range(size):
                node = bfs.popleft()
                maxi = max(maxi, node.val)
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
            ans.append(maxi)
        return ans


node = TreeNode(1)
node2 = TreeNode(3)
node3 = TreeNode(2)
node4 = TreeNode(5)
node5 = TreeNode(3)
node6 = TreeNode(9)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.right = node6

solution = Solution()
print(solution.largestValues(node))

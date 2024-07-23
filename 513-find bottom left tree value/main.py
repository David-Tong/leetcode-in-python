# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque
        bfs = deque()
        bfs.append(root)

        ans = root.val
        while bfs:
            for x in range(len(bfs)):
                node = bfs.popleft()
                if x == 0:
                    ans = node.val
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
        return ans


"""
node = TreeNode(2)
node2 = TreeNode(1)
node3 = TreeNode(3)

node.left = node2
node.right = node3
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
node3.left = node5
node3.right = node6
node5.left = node7

solution = Solution()
print(solution.findBottomLeftValue(node))

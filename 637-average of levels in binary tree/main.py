class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        from collections import deque
        bfs = deque()
        bfs.append(root)

        ans = list()
        while bfs:
            size = len(bfs)
            total = 0
            for x in range(size):
                curr = bfs.popleft()
                total += curr.val
                if curr.left:
                    bfs.append(curr.left)
                if curr.right:
                    bfs.append(curr.right)
            ans.append(total * 1.0 / size)

        return ans


"""
node = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)

node.left = node2
node.right = node3
node3.left = node4
node3.right = node5
"""

node = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5

solution = Solution()
print(solution.averageOfLevels(node))
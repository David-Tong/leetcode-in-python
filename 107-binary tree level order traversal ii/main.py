class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        from collections import deque
        bfs = deque()
        bfs.append(root)
        levels = []
        while len(bfs) > 0:
            level = []
            length = len(bfs)
            for x in range(length):
                node = bfs.popleft()
                level.append(node.val)
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
            levels.append(level)

        return levels[::-1]


node = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)

node.left = node2
node.right = node3
node3.left = node4
node3.right = node5

solution = Solution()
print(solution.levelOrderBottom(node))

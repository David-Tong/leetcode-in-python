class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def getDepth(node):
            if not node:
                return 0
            else:
                return max(getDepth(node.left), getDepth(node.right)) + 1

        m = getDepth(root)
        n = 2 ** m - 1
        ans = [[""] * n for _ in range(m)]

        from collections import deque
        bfs = deque()
        bfs.append((root, (n - 1) // 2))
        row = 0
        while bfs:
            size = len(bfs)
            for x in range(size):
                node, c = bfs.popleft()
                ans[row][c] = str(node.val)
                if node.left:
                    bfs.append((node.left, c - 2 ** (m - row - 2)))
                if node.right:
                    bfs.append((node.right, c + 2 ** (m - row - 2)))
            row += 1

        return ans


node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)

node.left = node2
node.right = node3
node2.right = node4

solution = Solution()
print(solution.printTree(node))

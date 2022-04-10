class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque
        bfs = deque()
        bfs.append((root, 1))
        ans = 0
        while bfs:
            length = len(bfs)
            ans = max(ans, bfs[-1][1] - bfs[0][1] + 1)
            for x in range(length):
                (node, id) = bfs.popleft()
                if node.left:
                    bfs.append((node.left, id * 2))
                if node.right:
                    bfs.append((node.right, id * 2 + 1))
        return ans


node = TreeNode(1)
node2 = TreeNode(3)
node3 = TreeNode(2)
node4 = TreeNode(5)
node5 = TreeNode(3)
node6 = TreeNode(9)
node7 = TreeNode(7)

node.left = node2
node.right = node3
node2.left = node4
node3.right = node5
node4.left = node6
node5.right = node7


solution = Solution()
print(solution.widthOfBinaryTree(node))

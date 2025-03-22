# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # pre-process
        from collections import deque
        bfs = deque()

        # process
        # bfs
        bfs.append(root)
        level = 1
        while bfs:
            size = len(bfs)
            if level % 2 == 0:
                nodes = list()
                values = list()

            for _ in range(size):
                curr = bfs.popleft()
                if level % 2 == 0:
                    nodes.append(curr)
                    values.append(curr.val)
                if curr.left:
                    bfs.append(curr.left)
                if curr.right:
                    bfs.append(curr.right)

            if level % 2 == 0:
                values = values[::-1]
                for x in range(size):
                    nodes[x].val = values[x]
            level += 1

        return root


node = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(5)
node4 = TreeNode(8)
node5 = TreeNode(13)
node6 = TreeNode(21)
node7 = TreeNode(34)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

solution = Solution()
print(solution.reverseOddLevels(node))

node
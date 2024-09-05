# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        # pre-process
        from collections import defaultdict
        paths = defaultdict(list)

        def doPath(node):
            if node.left:
                paths[node.val].append((node.left.val, "L"))
                paths[node.left.val].append((node.val, "U"))
                doPath(node.left)
            if node.right:
                paths[node.val].append((node.right.val, "R"))
                paths[node.right.val].append((node.val, "U"))
                doPath(node.right)

        doPath(root)

        # bfs
        from collections import deque
        bfs = deque()
        visited = defaultdict(bool)
        node = startValue
        bfs.append((node, ""))
        visited[node] = True

        ans = ""
        while bfs:
            curr, path = bfs.popleft()
            for nxt, pth in paths[curr]:
                if not visited[nxt]:
                    bfs.append((nxt, path + pth))
                    visited[nxt] = True
                if nxt == destValue:
                    ans = path + pth
                    return ans
        return ans


"""
node = TreeNode(5)
node2 = TreeNode(1)
node3 = TreeNode(2)
node4 = TreeNode(3)
node5 = TreeNode(6)
node6 = TreeNode(4)

node.left = node2
node.right = node3
node2.left = node4
node3.left = node5
node3.right = node6

startValue = 3
destValue = 6

startValue = 2
destValue = 4

startValue = 6
destValue = 4

startValue = 5
destValue = 4

node = TreeNode(2)
node2 = TreeNode(1)

node.left = node2

startValue = 2
destValue = 1
"""

node = TreeNode(5)
node2 = TreeNode(8)
node3 = TreeNode(3)
node4 = TreeNode(1)
node5 = TreeNode(4)
node6 = TreeNode(7)
node7 = TreeNode(6)
node8 = TreeNode(2)

node.left = node2
node.right = node3
node2.left = node4
node3.left = node5
node3.right = node6
node4.left = node7
node7.right = node8

startValue = 5
destValue = 6

solution = Solution()
print(solution.getDirections(node, startValue, destValue))

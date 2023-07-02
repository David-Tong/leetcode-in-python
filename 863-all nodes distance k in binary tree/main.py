# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        self.path = list()

        def findTarget(node, target, path):
            if node == target:
                for _ in path:
                    self.path.append(_)
                self.path.append(node)
                return True

            if node.left:
                if findTarget(node.left, target, path + [node]):
                    return True
            if node.right:
                if findTarget(node.right, target, path + [node]):
                    return True
            return False

        findTarget(root, target, list())

        # post-process
        from collections import defaultdict
        reversed_path = defaultdict(TreeNode)
        for x in range(1, len(self.path)):
            reversed_path[self.path[x]] = self.path[x - 1]

        # bfs
        from collections import deque
        bfs = deque()
        bfs.append(target)
        visited = defaultdict(bool)
        visited[target] = True

        ans = list()
        count = 0
        while bfs:
            size = len(bfs)
            for _ in range(size):
                node = bfs.popleft()
                if count == k:
                    ans.append(node.val)
                if node.left and not visited[node.left]:
                    visited[node.left] = True
                    bfs.append(node.left)
                if node.right and not visited[node.right]:
                    visited[node.right] = True
                    bfs.append(node.right)
                if node in reversed_path:
                    if not visited[reversed_path[node]]:
                        visited[reversed_path[node]] = True
                        bfs.append(reversed_path[node])
            if count == k:
                break
            count += 1
        return ans


"""
node = TreeNode(3)
node2 = TreeNode(5)
node3 = TreeNode(1)
node4 = TreeNode(6)
node5 = TreeNode(2)
node6 = TreeNode(0)
node7 = TreeNode(8)
node8 = TreeNode(7)
node9 = TreeNode(4)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node5.left = node8
node5.right = node9

target = node2
k = 2
"""

node = TreeNode(1)
target = node
k = 3

solution = Solution()
print(solution.distanceK(node, target, k))
